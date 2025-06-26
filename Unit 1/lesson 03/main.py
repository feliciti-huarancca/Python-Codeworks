BOOKS = [
    {
      'title': '1984',
      'genre': 'Dystopian',
      'rating': 9.0
    },
    {
      'title': 'Encuentra tu persona vitamina',
      'genre': 'Self-Help',
      'rating': 8.8
    },
    {
      'title': 'To Kill a Mockingbird',
      'genre': 'Fiction',
      'rating': 8.5
    },
    {
      'title': 'The Great Gatsby',
      'genre': 'Classic',
      'rating': 8.0
    },
    {
      'title': 'Brave New World',
      'genre': 'Dystopian',
      'rating': 9.2
    },
    {
      'title': 'Pride and Prejudice',
      'genre': 'Romance',
      'rating': 8.7
    },
    {
      'title': 'The Catcher in the Rye',
      'genre': 'Fiction',
      'rating': 8.3
    },
    {
      'title': 'Moby',
      'genre': 'Classic',
      'rating': 7.9
    }
]

def print_books(books_list):
    print('This is your book recomendation: \n')
    for book in books_list:
        print(f' 📕 {book['title']} | {book['genre']} | {book['rating']}')

print_books(BOOKS)

def book_recommendation_system(books_list):
    genre = input('Enter your preferred genre (Dystopian, Self-Help, Fiction, Classic, Romance): ')
    min_rating = input('Enter the minimum rating (0-10): ')

    new_list = [book for book in books_list if book['genre'] == genre]
    #for book in books_list:
    #    if book['genre'] == genre:
    #        print(f'This is the book I recomend: {book['title']} | {book['genre']} | {book['rating']}')
    print('This is the books I recommend: \n')
    print_books(new_list)

book_recommendation_system(BOOKS)