from email_validator import EmailNotValidError, validate_email
from flet import *
from features.users import auth_service
from features.users.auth_service import AuthService
import email_validator

class LoginPageController:
    def __init__(self, page:Page, auth_serv : AuthService):
        self.page = page
        self.auth_serv = auth_serv

    def authenticate_user(self, email, password):
        if not validate_email(email):
            return "Please enter a valid email address"

        response = self.auth_serv.login(email, password)
        print(response)
        #if response[0] == "Login successful":
            #self.page.client_storage

        return


    def validate_email(self, email):
        try:
            email_info = email_validator.validate_email(email, check_deliverability=False)
            return email_info.normalized
        except EmailNotValidError as e:
            return False

