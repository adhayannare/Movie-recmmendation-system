"""Content-based movie recommender using TF-IDF and cosine similarity."""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class MovieRecommender:
    def __init__(self, csv_path="data/movies.csv"):
        self.df = pd.read_csv(csv_path).fillna("")
        # Genres are repeated so they weigh more than the plot overview.
        self.df["soup"] = (self.df["genres"] + " ") * 3 + self.df["overview"]
        tfidf = TfidfVectorizer(stop_words="english")
        matrix = tfidf.fit_transform(self.df["soup"])
        self.similarity = linear_kernel(matrix, matrix)
        self.indices = pd.Series(self.df.index, index=self.df["title"].str.lower())

    def titles(self):
        return sorted(self.df["title"].tolist())

    def find_title(self, query):
        """Exact match first, then partial match."""
        q = query.strip().lower()
        if q in self.indices.index:
            return self.df.loc[self.indices[q], "title"]
        matches = self.df[self.df["title"].str.lower().str.contains(q, regex=False)]
        return matches.iloc[0]["title"] if not matches.empty else None

    def recommend(self, title, n=5):
        matched = self.find_title(title)
        if matched is None:
            return None
        idx = self.indices[matched.lower()]
        scores = sorted(enumerate(self.similarity[idx]), key=lambda x: x[1], reverse=True)
        top = [s for s in scores if s[0] != idx][:n]
        result = self.df.iloc[[i for i, _ in top]][["title", "year", "genres"]].copy()
        result["similarity"] = [round(float(s), 3) for _, s in top]
        return result.reset_index(drop=True)
