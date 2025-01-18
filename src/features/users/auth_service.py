from features.users.user import User
import bcrypt
import json
import requests

from utils.constants import SERVER_LINK


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service
        self.logged_in_user = User(1, "admin", "admin", [], [])


    def login(self, email, password):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        data = json.dumps({"email": email, "password_hash": password_hash})
        r = requests.post(SERVER_LINK + "/login", data)
        response_data = r.json()
        response_code = r.status_code
        access_token = None
        refresh_token = None
        if response_code == 201:
            access_token = response_data['access_token']
            refresh_token = response_data['refresh_token']

        return access_token, refresh_token


    def register(self, email, password):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        data = json.dumps({"email": email, "password_hash": password_hash})
        r = requests.post(SERVER_LINK+"/register", data)
        return r


    def logout(self):
        self.logged_in_user = None


    def validate_password(self, user: User, password: str):
        return True