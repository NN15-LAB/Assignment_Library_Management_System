class Book:
    def __init__(self, title, author, isbn, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {self.availability}"

    def update_availability(self, availability):
        self.availability = availability


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"
