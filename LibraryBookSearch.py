books = {
    "Harry Potter 1": {"Author": "J.K. Rowling", "Language": "English", "Page": 100, "Book Type": "Fantasy book"},
    "Herr der Diebe": {"Author": "Cornelia Funke", "Language": "German", "Page": 100, "Book Type": "Children's Fiction"}
}


book_name = input("Which book are you looking for? ")


if book_name in books:
    book = books[book_name]
    print(f"Book Name: {book_name}")
    print(f"Author: {book['Author']}")
    print(f"Language: {book['Language']}")
    print(f"Pages: {book['Page']}")
    print(f"Book Type: {book['Book Type']}")
else:
    print("This book is not available in our database.")
