import re
from werkzeug.security import hmac


class UserUtils:

    @staticmethod
    def _username_is_valid(username: str) -> bool:
        username_matcher = re.compile(r"^[A-Za-z0-9{2,}]+$")
        return True if username_matcher.match(username) else False

    @staticmethod
    def _email_is_valid(email: str) -> bool:
        email_matcher = re.compile(r"^[\w-]+@([\w]+\.)+[\w]+[\.+A-Za-z{2,}]+$")
        return True if email_matcher.match(email) else False

    @staticmethod
    def _password_is_valid(password: str) -> bool:
        password_matcher = re.compile(
            r"^(?=.{10,15}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[\!\@\#\$\%\^\&\*\-\=\+\_\<\>\{\}\(\)\[\]\:\;\/\|\~\`\ ]).*$")
        return True if password_matcher.match(password) else False


class LoginUtils(UserUtils):
    @staticmethod
    def _valid_login(name_email: str, password: str) -> bool:
        return True if (UserUtils._email_is_valid(name_email) or
                        UserUtils._username_is_valid(name_email)) and \
                       UserUtils._password_is_valid(password) else False


class RegisterUtils(UserUtils):
    @staticmethod
    def _valid_register(username: str, email: str, password: str, re_password: str) -> bool:
        return True if UserUtils._username_is_valid(username) and \
                       UserUtils._email_is_valid(email) and \
                       UserUtils._password_is_valid(password) and \
                       UserUtils._password_is_valid(re_password) and \
                       password == re_password else False
