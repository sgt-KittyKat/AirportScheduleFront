from features.users import auth_service
from features.users.auth_service import AuthService


class LoginPageController:
    def __init__(self, auth_serv : AuthService):
        self.auth_serv = auth_serv

    def authenticate_user(self, email, password):
        return self.auth_serv.login(email, password)
