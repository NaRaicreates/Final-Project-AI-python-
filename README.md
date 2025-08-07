# Final-Project-AI-python-
movie recommendation 
This is a final project built using **streamlit** and **TMDB API** The app recommends movies based on the selected genre, minimum release year, and rating. it provides movie posters, overviews, and basic metadata.

---

## project objective 
The goal of this project in to create a **simple, interactive movie recommendation system** that allows users to:
- selected their preferred movie genre,
- filter movies by minimum release year and rating,
- get visually engaging result via TMDB posters and descriptions.

  This project also demonstrates the use of APIs, Pythonfunction, streamlit interface, and app deployment.

---
## project structure
final-project-movie-recommender/
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── .streamlit/
│ └── secrets.toml # API key (not included in GitHub)
└── README.md # Project documentation

--- 

## how to run the app Locally 

1. **clone the repository**:
```bash
git clone https://github.com/NaRaicreates/Final-Project-AI-python-.git
```
2. pip install - requirements.txt
3. create .streamlit/secrets.toml file with this content :
   [API]
   TMDB_KEY = "your_tmdb_api_key"
4. run the app : streamlit run app.py

----

Live App(Deployed on Streamlit Cloud 
https://hvwcmvuweneeq6vfmcfzaj.streamlit.app/

---

Features : 
- genre based filtering
- minimum release year selector
- rating filter
- poster and overviw display for each movie
- realtime data from TMDB API
- Clean interface with streamlit widgets

**Authors**
Name : Nabila raisa sofa 
github: https://github.com/NaRaicreates/Final-Project-AI-python-.git
course : final project - AI and python
