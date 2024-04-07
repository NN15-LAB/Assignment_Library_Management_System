class CheckInOut:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager

    def check_out_book(self, isbn, user_id):
        book = self._find_book(isbn)
        user = self._find_user(user_id)
        if book and user:
            if book.availability:
                book.update_availability(False)
                print(f"Book '{book.title}' checked out by '{user.name}'")
            else:
                print(f"Book '{book.title}' is not available for checkout")
        else:
            print("Book or user not found")

    def check_in_book(self, isbn):
        book = self._find_book(isbn)
        if book:
            book.update_availability(True)
            print(f"Book '{book.title}' checked in successfully")
        else:
            print("Book not found")

    def _find_book(self, isbn):
        books = self.book_manager.search_by_isbn(isbn)
        return books[0] if books else None

    def _find_user(self, user_id):
        users = self.user_manager.search_by_user_id(user_id)
        return users[0] if users else None
