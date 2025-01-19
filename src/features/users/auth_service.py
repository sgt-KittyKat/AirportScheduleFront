from features.users.user import User
import bcrypt
import json
import requests

from utils.constants import SERVER_LINK


class AuthService:
    def __init__(self):
        self.logged_in_user = User(1, "admin", "admin", [], [])

    def login(self, email, password):
        #password_hash = str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
        password_hash = password
        data = json.dumps({"email": email, "password_hash": password_hash})
        headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
        with requests.Session() as session:
            r = requests.post(SERVER_LINK + "/login", data, headers=headers)
            response_data = r.json()
            response_code = r.status_code
            print(r.headers)
            if response_code == 200:
                session_id = r.cookies.get("session")
                return {"success": True, "message": "Login successful", "session_id": session_id}
            else:
                return {"success": False, "message": response_data.get("error", "Invalid credentials")}


    def register(self, email, password):
        #password_hash = str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
        password_hash = password
        data = json.dumps({"email": email, "password_hash": password_hash})

        r = requests.post(SERVER_LINK+"/register", data, headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'})
        response_data = r.json()
        response_code = r.status_code
        if response_code == 201:
            return "Registration successful"
        return response_data.get("error", "Something went wrong")



    def logout(self):
        self.logged_in_user = None


    def validate_password(self, user: User, password: str):
        return True