# Movie-Recommender-System
python and Machine Learning 


How the Recommended system works?
Any platforms like Netflix , Amazon, etc.. recommends various things  based on our Behavior, ratings, interest and tags(keywords that we are using in the searchbox).
There are 2 types of Recommendation Systems.
1) **Content based** which works on **tags.**
2) **Collaborative** which works on other 3 factors which I've mention earlier.

->In this project, I've worked on **Content based** Recommendation System.
-> Let's say I've searched for Avengers which is action movie so it has tag Action so based on this tag system recommend me Iron Movie and other Avenger's movies.

-> In this project I have dataset with 10,000 records.
-> I have applied feature engineering on the dataset to prepare a new column called Tags(Overview + genre). 
-> Tags column was originally in text format so I've vectorized it(Convert to unit vectors) using **CountVectorizer** function of Sklearn library.
-> After that I am going to calculate **cosine similarity** which means suppose I have max 10,000 dimensions and I am not going to count the eucleadian distance of dimensions but I am going to calcuate **theta** angle     
   between the 2 dimensions to check their distance.
-> At last created a function that try to access similarity values of searched movie based on vectors.
    
-> Using streamlit functionality of Python I've created front-end to embed this model.
