import json
from models import Book, User

class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return obj.__dict__
        elif isinstance(obj, User):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

class Storage:
    @staticmethod
    def save_data(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, cls=BookEncoder)

    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []
