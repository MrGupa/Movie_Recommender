import streamlit as st
import pickle
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

st.title("Movies Recommendation")

movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Setup requests session with retries
session = requests.Session()
retry = Retry(connect=3, backoff_factor=2)  # retry 3 times with exponential backoff
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2736a08daef7a534d3cf2d8c371e0427&language=en-US"
    try:
        response = session.get(url, timeout=10)  # timeout after 10 seconds
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except Exception as e:
        st.warning(f"⚠️ Could not fetch poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].Title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

movie_list = movies['Title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list, index=None)

if st.button("Show Recommendation") and selected_movie:
    recommned_movies_names, recommended_movies_posters = recommend(selected_movie)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommned_movies_names[i])
            st.image(recommended_movies_posters[i])
