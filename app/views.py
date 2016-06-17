from flask import render_template, flash, redirect, request
from flask_wtf import Form
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, \
    PasswordField
from wtforms.validators import Required
from flask_login import login_user
from app import app
from app import dbi
import sys
print(sys.path)
#from dbi import User


class LoginForm(Form):
    username = TextField('',
    validators=[Required()],
    render_kw={"placeholder": "username"})

    password = PasswordField('',
    validators=[Required()],
    render_kw={"placeholder": "password"})
    submit_button = SubmitField('log in')

@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Handles user logins
    """
    form = LoginForm()
    form.validate_on_submit()  # to get error messages to the browser
    return render_template('login.html',
                           title='Sign In',
                           form=form
                           )


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        username = request.form['username']
        password = request.form['password']
    except Exception as e:
        return render_template('login.html',
                                   title='Sign In',
                                   form=request.form,
                                   error=str(e)
                                   )

@app.route('/users')
def users():
    user_details = dbi.User.get_user_details()
    return render_template('users.html',
                           title='Users',
                           user_details=user_details
                           )


@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home'
                           )
