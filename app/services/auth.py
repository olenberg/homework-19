import calendar
import datetime
import jwt
from app.services.user import UserService
from app.constants import SECRET, ALGO


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if user is None:
            return False

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                return False

        data = {
            "username": user.username,
            "role": user.role
        }

        # access token on 30 min
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        # refresh token on 30 days
        days100 = datetime.datetime.utcnow() + datetime.timedelta(days=100)
        data["exp"] = calendar.timegm(days100.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, SECRET, algorithms=[ALGO])
        username = data["username"]
        user = self.user_service.get_by_username(username)

        if user is None:
            return False

        return self.generate_tokens(username, user.password, is_refresh=True)
