import streamlit as st 
import requests 

API_KEY = st.secrets["API"]["TMDB_KEY"]
TMDB_BASE_URL = "https://api.themoviedb.org/3"

@st.cache_data 
def get_genres():
    url = f"{TMDB_BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    #st.write("DEBUG - Status Code:", response.status_code)
    #st.write("DEBUG - Response JSON:", response.json())
    if response.status_code != 200 or "genres" not in response.json():
        st.error("Failed to fetch genres. please check your API key and internet connection.")
        return {}
    genres = response.json()["genres"]
    return {genre["name"]: genre["id"] for genre in genres}

def get_recommendations(genre_id, min_year, min_rating):
    url = (
        f"{TMDB_BASE_URL}/discover/movie?"
        f"api_key={API_KEY}"
        f"&with_genres={genre_id}"
        f"&primary_release_date.gte={min_year}-01-01"
        f"&vote_average.gte={min_rating}"
        f"&sort_by=popularity.desc"
    )
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Failed to fetch recommendations. please check your internet connection.😜")
        return []
    return response.json()["results"]

st.title("🎬 Film recommendations!!!")
st.write("welcome to the movie recommendation app! choose a genre, set the year and rating, and get personalized movie recommendations!")

genres = get_genres()
genre_name = st.selectbox("Chose genre", list(genres.keys()))
min_year = st.slider("years realease", 1980, 2025, 2000)
min_rating = st.slider("movies rate ", 0.0, 10.0, 7.0, step=0.1)

    # Removed unexpected indentation and duplicate recommendation display block.
                
num_movies = st.slider("film can be showed", 1, 20, 5)

if st.button("Show Recommendations"):
    genre_id = genres[genre_name]
    movies = get_recommendations(genre_id, min_year, min_rating)

    if not movies:
        st.warning("No recommendation can be found.")
    else:
        for movie in movies[:num_movies]:
            st.subheader(movie["title"])
            st.write(movie["overview"] or "Sorry, No description about this movie.")
            poster_path = movie["poster_path"]
            if poster_path:
                poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                st.image(poster_url, width=300)


