# Library Management:

# Initialize the library books list
books = []

def add_book(book_name):
    """Add a book to the library."""
    books.append(book_name)
    print(f'Book "{book_name}" has been added to the library.')

def borrow_book(book_name):
    """Borrow a book from the library."""
    if book_name in books:
        books.remove(book_name)
        print(f'You have borrowed "{book_name}".')
    else:
        print(f'Sorry, "{book_name}" is not available in the library.')

def return_book(book_name):
    """Return a book to the library."""
    books.append(book_name)
    print(f'You have returned "{book_name}".')

def show_available_books():
    """Display the list of available books."""
    if books:
        print("Available books in the library:")
        for i in books:
            print(f"- {i}")
    else:
        print("No books are currently available in the library.")

# Main program loop
while True:
    user_input = input("\nChoose an option: \n1. Add a Book \n2. Borrow a Book \n3. Return a Book \n4. Show Available Books \n5. Exit\n")

    if user_input == '1':
        book = input("Enter the name of the book to add: ")
        add_book(book)

    elif user_input == '2':
        book = input("Enter the name of the book to borrow: ")
        borrow_book(book)

    elif user_input == '3':
        book = input("Enter the name of the book to return: ")
        return_book(book)

    elif user_input == '4':
        show_available_books()

    elif user_input == '5':
        print("Exiting the system. Have a nice day!")
        break

    else:
        print("Invalid option. Please try again.")


# books = []

# def add_book(book_name):
#     """Add a book to the library."""
#     books.append(book_name)
#     print(f'Book "{book_name}" has been added to the library.')

# def borrow_book(book_name):
#     """Borrow a book from the library."""
#     if book_name in books:
#         books.remove(book_name)
#         print(f'You have borrowed "{book_name}".')
#     else:
#         print(f'Sorry, "{book_name}" is not available in the library.')

# def return_book(book_name):
#     """Return a book to the library."""
#     books.append(book_name)
#     print(f'You have returned "{book_name}".')

# def show_available_books():
#     """Display the list of available books."""
#     if books:
#         print("Available books in the library:")
#         for book in books:
#             print(f"- {book}")
#     else:
#         print("No books are currently available in the library.")

# # Main program loop
# while True:
#     user_input = input("\nChoose an option: \n1. Add a Book \n2. Borrow a Book \n3. Return a Book \n4. Show Available Books \n5. Exit\n")

#     if user_input == '1':
#         book = input("Enter the name of the book to add: ")
#         add_book(book)

#     elif user_input == '2':
#         book = input("Enter the name of the book to borrow: ")
#         borrow_book(book)

#     elif user_input == '3':
#         book = input("Enter the name of the book to return: ")
#         return_book(book)

#     elif user_input == '4':
#         show_available_books()

#     elif user_input == '5':
#         print("Exiting the system. Have a nice day!")
#         break

#     else:
#         print("Invalid option. Please try again.")


# def show():
#     pass
# show()

i=0

while():
    i+=1