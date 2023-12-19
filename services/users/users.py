from models.user import User

def create_user(first_name: str, last_name: str) -> str:
    new_user = User(first_name, last_name)
    return f'Added {new_user}'

def get_users() -> list:
    return User.all