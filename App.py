import os
import pickle
import requests
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Helpers
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_api_key():
    # First try Streamlit secrets, then fallback to environment variable
    try:
        return st.secrets["TMDB_API_KEY"]
    except Exception:
        return os.getenv("TMDB_API_KEY", "")

def fetch_poster(movie_id):
    api_key = get_api_key()
    if not api_key:
        return "https://via.placeholder.com/500x750?text=No+API+Key"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception:
        return "https://via.placeholder.com/500x750?text=Error+Loading"

@st.cache_data
def load_movies():
    file_path = os.path.join(BASE_DIR, "movies_list.pkl")
    with open(file_path, "rb") as f:
        movies = pickle.load(f)
    return movies

@st.cache_resource
def compute_similarity(tags):
    cv = CountVectorizer(max_features=10000, stop_words="english")
    vectors = cv.fit_transform(tags.fillna("").astype(str)).toarray()
    similarity_matrix = cosine_similarity(vectors)
    return similarity_matrix

def recommend(movie, movies, similarity):
    movie_index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []
    recommended_posters = []

    for i in distances[1:11]:
        idx = i[0]
        movie_id = movies.iloc[idx]["id"]
        title = movies.iloc[idx]["title"]

        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# -----------------------------
# Load data
# -----------------------------
movies = load_movies()
similarity = compute_similarity(movies["tags"])

# -----------------------------
# UI
# -----------------------------
st.title("🎬 Movie Recommender System")
st.write("Get movie recommendations based on content similarity.")

selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

if st.button("Show Recommendations"):
    movie_names, movie_posters = recommend(selected_movie, movies, similarity)

    st.subheader("Recommended Movies")

    cols = st.columns(5)
    for i in range(10):
        with cols[i % 5]:
            st.image(movie_posters[i], width=180)
            st.caption(movie_names[i])

# -----------------------------
# Footer note
# -----------------------------
if not get_api_key():
    st.warning("TMDb API key not found. Add it in Streamlit secrets as TMDB_API_KEY.")
