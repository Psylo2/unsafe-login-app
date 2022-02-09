from flask import request, flash, session

from usecases import UserUseCase
from logic.services import UserLogicService

from models.user import User, UserValidator
from models.password import Password


class UserLogic(UserUseCase, UserLogicService):
    def __init__(self):
        self._validator = UserValidator()

    def login(self) -> bool:
        name_email = request.form.get('name_email')
        password = request.form.get('password')

        if self._is_valid_login(name_email, password):
            user = User.find_from_db(name_email)
            user_pas = Password.find_from_db(name=user.name)
            if user and user_pas._current_password == password:
                session.clear()
                session['name_email'] = user.name
                flash(f'Welcome {user.name}', 'danger')

                return True

        flash('Invalid Inputs', 'danger')
        return False

    def register(self) -> bool:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        re_password = request.form.get('re_password')

        if self._is_valid_register(username=username, email=email,
                                   password=password, re_password=re_password):
            user = User(username, email, 0)
            user.save_to_db()
            pas = Password(username=user.name)
            if pas.confirm_password(password):
                pas._current_password = password
                pas.save_to_db()
                flash('Registration Success!', 'danger')
                return True

            flash('Password dont meet complexity!', 'danger')
            return False

        flash('Invalid Inputs', 'danger')
        return False

    def change_password(self) -> bool:
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            re_password = request.form.get('re_password')

            if self._is_valid_register(username=username, email=email,
                                       password=password, re_password=re_password):
                user = User.find_from_db(username)
                if user:
                    new_passw = Password(username=username)
                    if new_passw.confirm_password(password):
                        new_order = new_passw.order_new_password(username=user.name,
                                                                 password=password)
                        new_passw.update_to_db(new_order)
                        flash('Password Changed!', 'danger')
                        return True

            flash('Invalid Inputs', 'danger')
            return False

    def logout(self) -> None:
        flash('Farewell', 'danger')
        session['name_email'] = None

    def _is_valid_login(self, name_email: str, password: str) -> bool:
        return True if self._valid_login(name_email=name_email,
                                         password=password) else False

    def _is_valid_register(self, username: str, email: str, password: str, re_password: str) -> bool:
        return True if self._valid_register(username=username, email=email,
                                            password=password, re_password=re_password) else False

    def _valid_login(self, name_email: str, password: str) -> bool:
        return (self._validator.is_valid_email(email=name_email) or
                self._validator.is_valid_username(username=name_email)) and \
               self._validator.is_valid_password(password=password)

    def _valid_register(self, username: str, email: str, password: str, re_password: str) -> bool:
        return self._validator.is_valid_username(username) and \
               self._validator.is_valid_email(email) and \
               self._validator.is_valid_password(password) and \
               self._validator.is_valid_password(re_password) and \
               password == re_password
