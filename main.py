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
            
        self.user_manager.users = self.storage.load_data("users.json")

    def save_data(self):
        # Save data to storage
        self.storage.save_data(self.book_manager.books, "books.json")
        self.storage.save_data(self.user_manager.users, "users.json")

    def display_main_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. Checkout Book")
        print("5. Exit")

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

if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.run()

