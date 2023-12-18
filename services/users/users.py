from models.user import User

def create_user(first_name, last_name):
    new_user = User(first_name, last_name)
    return f'Added {new_user}'

def get_users():
    return User.all