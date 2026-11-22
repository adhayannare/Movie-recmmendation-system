"""Command-line interface for the movie recommender."""
from recommender import MovieRecommender


def main():
    rec = MovieRecommender()
    print("=== Movie Recommendation System ===")
    print("Type a movie name (or 'list' to see all, 'quit' to exit)\n")
    while True:
        query = input("Movie you like: ").strip()
        if query.lower() in {"quit", "exit", "q"}:
            break
        if query.lower() == "list":
            print("\n".join(rec.titles()), "\n")
            continue
        result = rec.recommend(query)
        if result is None:
            print("Movie not found. Type 'list' to see available titles.\n")
        else:
            print(f"\nBecause you liked '{rec.find_title(query)}':\n")
            print(result.to_string(index=False), "\n")


if __name__ == "__main__":
    main()
