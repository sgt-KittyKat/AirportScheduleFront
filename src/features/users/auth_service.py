from features.users.user import User


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service
        self.logged_in_user = User(1, "admin", "admin", [], [])

    def login(self, username, password):
        # Example logic
        user = self.user_service.get_user_by_username(username)
        if user and self.validate_password(user, password):
            self.logged_in_user = user
            return user
        else:
            raise ValueError("Invalid credentials")

    def logout(self):
        self.logged_in_user = None

    def validate_password(self, user: User, password: str):
        return True