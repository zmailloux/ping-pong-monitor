import hashlib

import flask_login
from flask import (Blueprint, Flask, jsonify, redirect, render_template, request, send_file, session, url_for)
from utils.activity import (add_login_activity, add_user_activity, get_user_activity, load_json_file)

users = {'admin': {'password': '69bc0cc4b50ac0342dfcecdde7091587'}, 'user': {'password': '9e8acc5d49877acdb8837b032b7b9010'}}


login_view = Blueprint('login_view', __name__)
login_view.app_template_filter()

login_manager = flask_login.LoginManager()

def set_login_manager(app):
    login_manager.init_app(app)


class User(flask_login.UserMixin):
    pass


"""************* Login Logic (Don't mess with) *************"""
@login_view.route('/logout')
def logout():
    flask_login.logout_user()
    session['logged_in'] = False
    return redirect(url_for('login_view.login'))


@login_manager.user_loader
def user_loader(username):
    print(f"Username: {username}!!!")
    if username not in users:
        return

    user = User()
    user.id = username
    return user


#https://github.com/maxcountryman/flask-login
@login_view.route('/', methods=['GET', 'POST'])
@login_view.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not session.get('logged_in'):
            return render_template('login.html', build_info="test")
        else:
            print("going to index!")
            return redirect(url_for('index'))

    username = request.form['username']
    encoded_pw = str(hashlib.md5(request.form['password'].encode()).hexdigest())

    if encoded_pw == users[username]['password']:
        user = User()
        user.id = username
        # add_login_activity(username)
        flask_login.login_user(user)
        print("authed!")
        session['logged_in'] = True
        return redirect(url_for('index'))

    return 'Bad login'
