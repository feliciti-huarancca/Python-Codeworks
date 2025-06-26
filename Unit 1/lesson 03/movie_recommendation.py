
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
    {"title": "The Lord of the Rings: The Return of the King", "genre": "Fantasy", "rating": 8.9},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "Gladiator", "genre": "Action", "rating": 8.5},
    {"title": "The Departed", "genre": "Crime", "rating": 8.5},
    {"title": "The Social Network", "genre": "Drama", "rating": 7.7},
    {"title": "Jurassic Park", "genre": "Sci-Fi", "rating": 8.1},
    {"title": "Avatar", "genre": "Fantasy", "rating": 7.8}
]

def print_movies(movies_list):
    for movie in movies_list:
        print(f"🎬 {movie['title']} | {movie['genre']} | {movie['rating']}")

movies.append({"title": "The Silence of the Lambs", "genre": "Thriller", "rating": 8.6})

def movie_recommendation_system(movies_list):
    preferred_genre = input("Enter your preferred genre (Sci-Fi, Drama, Crime, Action, Fantasy, Thriller): ").upper()
    min_rating = float(input("Enter the minimum rating (0-10): "))

    movies_recommendations = [movie for movie in movies_list if movie['genre'].upper() == preferred_genre and movie['rating'] >= min_rating]
    
    if movies_recommendations:
        print_movies(movies_recommendations)
    else:
        print("We don't have any movies for you based on your preferences")

print("Welcome to the Movie Recommendation System!")
movie_recommendation_system(movies)