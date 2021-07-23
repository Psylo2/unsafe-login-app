import re


class UserUtils:

    @staticmethod
    def username_is_valid(username: str) -> bool:
        username_matcher = re.compile(r"^[A-Za-z0-9{2,}]+$")
        return True if username_matcher.match(username) else False

    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_matcher = re.compile(r"^[\w-]+@([\w]+\.)+[\w]+[\.+A-Za-z{2,}]+$")
        return True if email_matcher.match(email) else False

    @staticmethod
    def password_is_valid(password: str) -> bool:
        password_matcher = re.compile(
            r"^(?=.{10,15}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[\!\@\#\$\%\^\&\*\-\=\+\_\<\>\{\}\(\)\[\]\:\;\/\|\~\`\ ]).*$")
        return True if password_matcher.match(password) else False

