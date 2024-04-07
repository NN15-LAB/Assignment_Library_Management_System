from book import BookManager
from user import UserManager
from check import CheckInOut
from storage import Storage

class LibrarySystem:
    def __init__(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.checkout_manager = CheckInOut(self.book_manager, self.user_manager)
        self.storage = Storage()

        # Load data from storage
        book_data = self.storage.load_data("books.json")
        for book_info in book_data:
            self.book_manager.add_book(book_info['title'], book_info['author'], book_info['isbn'])

        user_data = self.storage.load_data("users.json")
        for user_info in user_data:
            self.user_manager.add_user(user_info['name'], user_info['user_id'])

    def save_data(self):
        # Save data to storage
        self.storage.save_data([book.__dict__ for book in self.book_manager.books], "books.json")
        self.storage.save_data([user.__dict__ for user in self.user_manager.users], "users.json")

    def display_main_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. Checkout Book")
        print("5. Search Book by Title")
        print("6. Search Book by Author")
        print("7. Search Book by ISBN")
        print("8. Update Book Information")
        print("9. Delete Book")
        print("10. List Users")
        print("11. Search User by Name")
        print("12. Search User by ID")
        print("13. Update User Information")
        print("14. Delete User")
        print("15. Check In Book")
        print("16. Exit")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter choice: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.list_books()
            elif choice == '3':
                self.add_user()
            elif choice == '4':
                self.checkout_book()
            elif choice == '5':
                self.search_book_by_title()
            elif choice == '6':
                self.search_book_by_author()
            elif choice == '7':
                self.search_book_by_isbn()
            elif choice == '8':
                self.update_book_info()
            elif choice == '9':
                self.delete_book()
            elif choice == '10':
                self.list_users()
            elif choice == '11':
                self.search_user_by_name()
            elif choice == '12':
                self.search_user_by_id()
            elif choice == '13':
                self.update_user_info()
            elif choice == '14':
                self.delete_user()
            elif choice == '15':
                self.check_in_book()
            elif choice == '16':
                print("Exiting.")
                self.save_data()  # Save data before exiting
                break
            else:
                print("Invalid choice, please try again.")

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        self.book_manager.add_book(title, author, isbn)
        print("Book added.")

    def list_books(self):
        self.book_manager.list_books()

    def add_user(self):
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        self.user_manager.add_user(name, user_id)
        print("User added.")

    def checkout_book(self):
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        self.checkout_manager.check_out_book(isbn, user_id)
        print("Book checked out.")

    def search_book_by_title(self):
        title = input("Enter title to search: ")
        found_books = self.book_manager.search_by_title(title)
        if found_books:
            print("Matching Books:")
            for book in found_books:
                print(book)
        else:
            print("No matching books found.")

    def search_book_by_author(self):
        author = input("Enter author to search: ")
        found_books = self.book_manager.search_by_author(author)
        if found_books:
            print("Books by Author:")
            for book in found_books:
                print(book)
        else:
            print("No books found by this author.")

    def search_book_by_isbn(self):
        isbn = input("Enter ISBN to search: ")
        found_books = self.book_manager.search_by_isbn(isbn)
        if found_books:
            print("Book with ISBN:")
            for book in found_books:
                print(book)
        else:
            print("No book found with this ISBN.")

    def update_book_info(self):
        isbn = input("Enter ISBN of the book to update: ")
        found_books = self.book_manager.search_by_isbn(isbn)
        if found_books:
            # Assuming there's only one book with a given ISBN for simplicity
            book = found_books[0]
            print("Current Book Information:")
            print(book)
            # Update book information
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            if title:
                book.title = title
            if author:
                book.author = author
            print("Book information updated.")
        else:
            print("No book found with this ISBN.")

    def delete_book(self):
        isbn = input("Enter ISBN of the book to delete: ")
        self.book_manager.delete_book(isbn)
        print("Book deleted.")

    def list_users(self):
        self.user_manager.list_users()

    def search_user_by_name(self):
        name = input("Enter name to search: ")
        found_users = self.user_manager.search_by_name(name)
        if found_users:
            print("Matching Users:")
            for user in found_users:
                print(user)
        else:
            print("No matching users found.")

    def search_user_by_id(self):
        user_id = input("Enter user ID to search: ")
        found_users = self.user_manager.search_by_user_id(user_id)
        if found_users:
            print("User with ID:")
            for user in found_users:
                print(user)
        else:
            print("No user found with this ID.")

    def update_user_info(self):
        user_id = input("Enter ID of the user to update: ")
        found_users = self.user_manager.search_by_user_id(user_id)
        if found_users:
            # Assuming there's only one user with a given ID for simplicity
            user = found_users[0]
            print("Current User Information:")
            print(user)
            # Update user information
            name = input("Enter new name (leave blank to keep current): ")
            if name:
                user.name = name
            print("User information updated.")
        else:
            print("No user found with this ID.")

    def delete_user(self):
        user_id = input("Enter ID of the user to delete: ")
        self.user_manager.delete_user(user_id)
        print("User deleted.")

    def check_in_book(self):
        isbn = input("Enter ISBN of the book to check in: ")
        self.checkout_manager.check_in_book(isbn)
        print("Book checked in.")


if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.run()
