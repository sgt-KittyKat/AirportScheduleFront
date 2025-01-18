class UserService:
    def __init__(self, dao):
        self.dao = dao
    def get_user_by_username(self, username: str):
        return self.dao.get_user_by_username(username)

