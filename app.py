"""Streamlit web app. Run with: streamlit run app.py"""
import streamlit as st
from recommender import MovieRecommender

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")


@st.cache_resource
def load():
    return MovieRecommender()


rec = load()
st.title("🎬 Movie Recommendation System")
st.write("Pick a movie you like and get similar suggestions.")

movie = st.selectbox("Choose a movie", rec.titles())
n = st.slider("Number of recommendations", 3, 10, 5)

if st.button("Recommend"):
    result = rec.recommend(movie, n)
    st.subheader(f"Because you liked {movie}:")
    st.dataframe(result, use_container_width=True, hide_index=True)
