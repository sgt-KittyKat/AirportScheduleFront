from email_validator import EmailNotValidError, validate_email
from flet import *

from features.users import auth_service
from features.users.auth_service import AuthService
import email_validator


class RegisterPageController:
    def __init__(self, page: Page, auth_serv: AuthService):
        self.page = page
        self.auth_serv = auth_serv

    def register_user(self, email, password, repeat_password):
        if not validate_email(email):
            return "Please enter a valid email address"

        if password != repeat_password:
            return "Passwords do not match"
        return self.auth_serv.register(email, password)


    def validate_email(self, email):
        try:
            email_info = email_validator.validate_email(email, check_deliverability=False)
            return email_info.normalized
        except EmailNotValidError as e:
            return False

