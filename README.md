# Movie-Recommender-System
🔍 Overview:

This project is a content-based movie recommendation system that suggests similar movies based on user input. It leverages machine learning and natural language processing techniques to analyze movie metadata and generate personalized recommendations.

The system focuses on transforming raw movie data into meaningful insights and delivering fast, interactive recommendations through a user-friendly interface.

🎯 Objective:

-> Build a recommendation engine that suggests movies similar to a given title

-> Apply machine learning techniques to understand movie similarity

-> Develop an interactive application for real-time recommendations

-> Optimize performance for faster response and better user experience

🧰 Tech Stack:

-> Python – Core programming

-> Pandas, NumPy – Data processing & manipulation

-> Scikit-learn – Machine learning (TF-IDF, cosine similarity)

-> Streamlit – Web application interface

-> TMDb API – Movie posters & metadata integration

📂 Dataset:

-> Movie metadata dataset (titles, genres, cast, overview, etc.)

-> Preprocessed to create meaningful textual features

-> Combined multiple attributes into a single feature for similarity computation

⚙️ How It Works:

1. Data Preprocessing
   
-> Cleaned and transformed raw movie data

-> Combined features like genres, cast, keywords, and overview

-> Removed noise and irrelevant information

2. Feature Engineering
   
-> Converted text data into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency)

-> Captured the importance of words across the dataset

3. Similarity Calculation
   
-> Computed cosine similarity matrix between movies

-> Identified movies with the highest similarity scores

4. Recommendation Engine
   
-> Input: Movie title

-> Output: Top N similar movies

-> Fast lookup using precomputed similarity matrix

5. Deployment
   
-> Built an interactive UI using Streamlit

-> Integrated TMDb API to display posters and enhance user experience

🚀 Features:

🎬- Movie recommendations based on similarity

⚡- Fast and efficient predictions

🖥️- Interactive web interface (Streamlit)

🧠- Machine learning-based recommendation logic

🎨- Visual display with movie posters

📊- Example Output

Input: Inception

Output: Interstellar, The Dark Knight, Shutter Island, Tenet…

📈 Key Highlights:

-> Built a scalable recommendation pipeline using NLP techniques

-> Reduced application load time by ~65% through optimization

-> Demonstrates end-to-end workflow: data preprocessing → modeling → deployment

💡 Learnings:

-> Practical implementation of recommender systems

-> Hands-on experience with NLP techniques (TF-IDF)

-> Understanding of similarity-based models

-> Deployment of ML models using Streamlit

<img width="1892" height="532" alt="home_landing_page" src="https://github.com/user-attachments/assets/8eb9f15b-3aed-4974-a648-6a0c6b927dbb" />

<img width="1907" height="827" alt="dropdown_for_movie_selection" src="https://github.com/user-attachments/assets/31ab51e9-8939-46af-a02a-db636fb74c10" />

<img width="1907" height="877" alt="Recommended_Movies" src="https://github.com/user-attachments/assets/4f692779-5dea-4ef3-afd2-d36760c714c4" />




