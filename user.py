import bcrypt
from schema.userdb import UserDb


class WrongHashedException(Exception):
    pass


class Encrypt:
    round = 12

    @staticmethod
    def get_hash(s: str) -> str:
        b_password = bytes(s, encoding='utf-8')
        hashed = bcrypt.hashpw(b_password, bcrypt.gensalt(Encrypt.round))
        if not bcrypt.checkpw(b_password, hashed):
            raise WrongHashedException()
        return hashed

    @staticmethod
    def is_match(s, h) -> bool:
        return bcrypt.checkpw(s, h)


class SignUp(object):

    def __init__(self, email: str = "", password: str = ""):
        self.email = email
        self.original_password = password
        self.hashed_password = self.encrypt_password(self.original_password)
        del self.original_password

    @staticmethod
    def encrypt_password(password: str) -> str:
        return Encrypt.get_hash(password)

    def create_user_if_exists(self) -> bool:
        return UserDb().create_user(self.email, self.hashed_password)


# TODO send email link
class SignIn(object):
    def check_account(self, email, password) -> bool:
        # select user's email and password from Database.

        return Encrypt.is_match(password, )
