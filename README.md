# 🎬 Movie Recommendation System

A content-based movie recommender built with Python. It suggests movies similar to one you like by comparing genres and plot descriptions.

## How it works
1. Genres and plot overview are combined into one text field per movie.
2. The text is converted to numeric vectors using **TF-IDF**.
3. **Cosine similarity** measures how close every pair of movies is.
4. The movies with the highest similarity to your pick are recommended.

## Tech stack
Python, Pandas, Scikit-learn, Streamlit

## Project structure
```
movie-recommendation-system/
├── data/movies.csv     # dataset
├── recommender.py      # recommendation engine
├── main.py             # command-line app
├── app.py              # Streamlit web app
├── requirements.txt
└── README.md
```

## Setup
```bash
git clone https://github.com/<your-username>/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
```

## Run
Command line:
```bash
python main.py
```
Web app:
```bash
streamlit run app.py
```

## Example
Input: `Inception` → Output: The Matrix, Interstellar, Avengers: Endgame, ...

## Future improvements
- Use the full MovieLens dataset (thousands of movies)
- Add collaborative filtering based on user ratings
- Show posters using the TMDB API
- Deploy on Streamlit Community Cloud

## Author
Your Name
