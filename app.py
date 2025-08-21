import streamlit as st
import pickle
import gzip
import pandas as pd
                            
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    # recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        # recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

def decompress_pickle(input_pkl_gz):
    with gzip.open(input_pkl_gz, 'rb') as f:
        return pickle.load(f)

st.title("Movie Recommendation System")

movie_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# similarity = pickle.load(open('similarity_com.pkl.gz', 'rb'))
similarity = decompress_pickle("similarity.pkl.gz")
# E:\SEM VII\Project 1\similarity.pkl
selected_movie = st.selectbox(
    "Select a movie to get recommendations", 
    movies['title'].values
)

if st.button('Recommend'):
    recommended_movie_names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        # st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        # st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        # st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        # st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        # st.image(recommended_movie_posters[4])