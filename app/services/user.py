import base64
import hashlib
import hmac
from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from app.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data.get("password"))
        return self.dao.create(data)

    def update(self, uid, data):
        user = self.get_one(uid)
        user.name = data.get("username")
        user.password = self.get_hash(data.get("password"))
        user.role = data.get("role")
        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    # def get_hash(self, password):
    #     return base64.b64encode(hashlib.pbkdf2_hmac(
    #         'sha256',
    #         password.encode('utf-8'),
    #         PWD_HASH_SALT,
    #         PWD_HASH_ITERATIONS
    #     ))
    #
    # def compare_passwords(self, password_hash, other_password):
    #     return hmac.compare_digest(
    #         base64.b64decode(password_hash),
    #         hashlib.pbkdf2_hmac('sha256', other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
    #     )

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'), # Convert the password to byte
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, hash_password, sec_password):
        return hmac.compare_digest(base64.b64decode(hash_password), base64.b64decode(self.get_hash(sec_password)))