from models import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                break

    def list_books(self):
        for book in self.books:
            print(book)

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        return found_books

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

    def search_by_isbn(self, isbn):
        found_books = [book for book in self.books if book.isbn == isbn]
        return found_books