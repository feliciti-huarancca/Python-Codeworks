LIBRARY = [
  {
    'title': 'How to train your dragon',
    'author': 'Cressida Cowell',
    'year': 2003,
  },
  {
    'title': 'Harry Potter and the Philosopher\'s Stone',
    'author': 'J.K. Rowling',
    'year': 1997,
  },
  {
    'title': 'The Hobbit',
    'author': 'J.R.R. Tolkien',
    'year': 1937,
  },
  {
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'year': 1925,
  },
  {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
  }
]

def save_library_to_file():
    with open('library.txt', 'w') as file:
        for item in LIBRARY:
            file.write(f'{item['title']} by {item['author']} in the {item['year']}\n')

def read_library_from_file():
    try:
      with open('library.txt', 'r') as file:
          print(f'****** Library Content 📚 ***\n{file.read()}')
    except FileNotFoundError:
        print('Library file not found 🥹. Please add books first.')

def add_book_to_library(title, author, year):
    LIBRARY.append({
        'title': title,
        'author': author,
        'year': year,
    })

def remove_book_from_library():
    print('Choose a book to remove from the library: ')

    for index, book in enumerate(LIBRARY):
        print(f"{index}. {book['title']} by {book['author']} ({book['year']})")

    choice = int(input('Enter the number of the book to remove: '))
    LIBRARY.pop(choice)

def library_management_system():
    try:
        while True:
            print('1. Add a book to the library\n2. View library content\n3. Remove book\n4. Exit')
            choice = input('\nEnter your choice: ')

            if choice == '1':
                title = input('Enter book title: ')
                author = input('Enter book author: ')
                year = int(input('Enter publication year: '))

                if year < 0:
                    raise Exception('This is not a valid year! 🤨')

                add_book_to_library(title, author, year)
                save_library_to_file()
                print(f'Book "{title}" by {author} in the {year} added to the library.')
            elif choice == '2':
                read_library_from_file()
            elif choice == '3':
                remove_book_from_library()
                save_library_to_file()
                print('Book removed from the library.')
            elif choice == '4':
                print('Exiting the library management system.')
                break
    except Exception as e:
        print(e)



#add_book_to_library('The Catcher in the Rye', 'J.D. Salinger', 1951)
#add_book_to_library('To Kill a Mockingbird', 'Harper Lee', 1960)
#
#save_library_to_file()
#read_library_from_file()

library_management_system()