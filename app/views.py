from flask import render_template, flash, redirect
from flask_wtf import Form
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, \
    PasswordField
from wtforms.validators import Required
from app import app


class LoginForm(Form):
    userid = TextField('userid',
    validators=[Required()],
    render_kw={"placeholder": "username"})

    password = PasswordField('Password',
    validators=[Required()],
    render_kw={"placeholder": "password"})
    submit_button = SubmitField('sign in')

@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Handles user logins
    """
    form = LoginForm()
    form.validate_on_submit()  # to get error messages to the browser
    return render_template('login2.html',
                           title='Sign In',
                           form=form
                           )


@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home'
                           )
