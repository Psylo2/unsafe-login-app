import functools
from typing import Callable
from flask import session, flash, redirect, url_for

def requires_login(fun: Callable) -> Callable:
    @functools.wraps(fun)
    def decorated_function(*args, **kwargs):
        if not session.get('name_email'):
            flash('You need to be singed in fot this page', 'danger')
            return redirect(url_for('users.login_get'))
        return fun(*args, **kwargs)
    return decorated_function