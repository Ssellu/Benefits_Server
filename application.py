#########################################################################################
# flask libs

# pip install flask
# pip install flask_sqlalchemy
#########################################################################################


#########################################################################################
# run server

# set FLASK_APP=C:\Users\issel\PycharmProjects\study_test\application
# flask run
#########################################################################################
from flask import Flask, flash, redirect, url_for, abort, request, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, lazy_gettext as _l
# from flask_bcrypt import Bcrypt
# from schema.dbModule import DataBase
from schema.user import UserDb
# from schema.model import User
# import token
import datetime
from config import Config

app = Flask(__name__)
# bcypt = Bcrypt(app)
babel = Babel(app)
app.config['DEBUG'] = True

app.config['LANGUAGES'] = {
    'en': 'English',
    'ko': 'Korean'
}
db = SQLAlchemy(app)


@babel.localeselector
def get_locale():
    print(f'{request.accept_languages.best_match(app.config["LANGUAGES"].keys())}')

    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

@app.route('/')
def main():
    return render_template('user/login.html')


@app.route('/login_chk', methods=["POST"])
def login_chk():
    pass
    # user = Userasdjalksjdlaksjdlkajsldkj
    # User.query.filter_by(u_mail=user.u_email).first()
    # if res is not None:
    #     return jsonify(result=True, u_id=res['u_id'])
    # return jsonify(result=False, u_id="aaaa")


@app.route('/signup', methods=["POST"])
def signup():
    content = request.json
    result = UserDb().create_user(email=content['email'], password=content['password'])
    if result:
        # 이메일 인증
        # t = token.generate_confirmation_token(content.email)
        print(result)
        return jsonify({'result': True, 'message': _l("Registration complete.")})
    return jsonify({'result': False, 'message': _l("Account exists.")})


# @app.route('/confirm/<t>')
# def confirm(t):
#     try:
#         email = token.confirm_token(t)
#     except:
#         flash(_l('The confirmation link is invalid or has expired.'), 'danger')
#     user = User.query.filter_by(email=email).first_or_404()
#     if user.confirmed:
#         flash(_l('Account already confirmed. Please login.'), 'success')
#     else:
#         user.confirmed = True
#         user.confirmed_on = datetime.datetime.now()
#         flash(_l('You have confirmed your account. Thanks!'), 'success')
#     return redirect(url_for('main.home'))




















