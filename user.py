from models import User

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users.append(new_user)

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                break

    def list_users(self):
        for user in self.users:
            print(user)

    def search_by_name(self, name):
        found_users = [user for user in self.users if user.name.lower() == name.lower()]
        return found_users

    def search_by_user_id(self, user_id):
        found_users = [user for user in self.users if user.user_id == user_id]
        return found_users
