from typing import Dict

from flask import request, flash

from usecases import AdminUseCase
from logic.services import AdminLogicService
from models.user import User
from models.password import PasswordConfig


class AdminLogic(AdminUseCase, AdminLogicService):
    def __init__(self):
        pass

    def users_list(self) -> str:
        users = User.find_all_from_db()
        return users

    def block_user(self, block) -> None:
        user = User.find_from_db(block)
        user.block_user_model()

    def unblock_user(self, unblock) -> None:
        user = User.find_from_db(unblock)
        user.unblock_user_model()

    def password_configuration(self) -> None:
        configurations = self.extract_configuration_fields(data=request.form)
        result = PasswordConfig.set_config(**configurations)
        if result:
            flash('Password Configuration Changed!', 'danger')
            return None

        flash('Invalid Inputs', 'danger')

    def configure_regex(self, data: Dict) -> str:
        re = ""
        re += "A-Z" if data.get('upper') == "1" else ""
        re += "a-z" if data.get('lower') == "1" else ""
        re += "0-9" if data.get('digits') == "1" else ""
        re += "\!\#\$\%\^\&\*\_\+\.\," if data.get('spec') == "1" else ""
        return re

    def extract_configuration_fields(self, data: dict) -> Dict:
        regex = self.configure_regex(data=data)
        use_dict = True if request.form.get('use_dict') == "1" else False
        return {
            "dictionary": use_dict,
            "regex": regex,
            "length": data.get('length'),
            "history": data.get('history'),
            "tries": data.get('tries')
        }
