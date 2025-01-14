from features.users.user import User


class FlightController:
    def get_user_flights(self, user:User):
        return user.upcoming_flights

    #def get_nav_bar(self):

