from flask import render_template, flash, redirect, request, url_for, session
from flask_wtf import Form
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, \
    PasswordField, SelectField
from wtforms.validators import Required

from app import app
from app import dbi
#from dbi import User


class LoginForm(Form):
    username = TextField('username',
                         validators=[Required()],
                         render_kw={"placeholder": "username"})

    password = PasswordField('password',
                             validators=[Required()],
                             render_kw={"placeholder": "password"})
    submit_button = SubmitField('log in')

    submit = SubmitField("sign in")


@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Handles user logins
    """
    form = LoginForm()
    if form.validate_on_submit():# to get error messages to the browse
        return redirect(url_for('index'))

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
        return redirect(url_for('login'))
    else:
        if dbi.check_pw(username, password):
            #get_user_details(required_columns="*", where_clause="%s", params=(1, )
            user_data = dbi.get_user_details(where_clause = "username = %s",
                                             params = (username, ))
            session["id"] = user_data[0]["id"]
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


@app.route('/users/')
@app.route('/users/<username>')
def users(username='all'):
    if username == 'all':
        where_clause = "%s"
        params = (1, )
    else:
        where_clause = "username = %s"
        params = (username, )
    user_details = dbi.get_user_details(where_clause=where_clause)
    return render_template('users.html',
                           title='Users',
                           user_details=user_details
                           )


@app.route('/test/')
def test():
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('index'))
    else:
        id = session["id"]
        data = dbi.get_user_details(where_clause="id = %s", params=(id, ))
        user_details = data[0]
        return render_template('test.html',
                               title='Test Page',
                               name=user_details["firstname"],
                               lastname=user_details["lastname"],
                               username=user_details["username"]
                               )


@app.route('/index')
def index():
    """ Home page """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))
    else:
        id = session["id"]
        data = dbi.get_user_details(where_clause="id = %s", params=(id, ))
        user_details = data[0]
        return render_template('index.html',
                               title='Home',
                               name=user_details["firstname"]
                               )

class CreateTicketForm(Form):
    phone_number = TextField('phone_number',
                            validators=[Required()],
                            render_kw={"placeholder": "Phone No of caller"})

    genders = []
    gender = SelectField('gender',
                         validators=[Required()],
                         choices=genders)

    provinces = []
    province = SelectField('province',
                         validators=[Required()],
                         choices=provinces)

    districts = []
    district = SelectField('district',
                         validators=[Required()],
                         choices=districts)

    submit_button = SubmitField('submit')



@app.route('/create_ticket')
def create_ticket():
    """ page for creating new tickets """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))
    else:
        id = session["id"]
        data = dbi.get_user_details(where_clause="id = %s", params=(id, ))
        user_details = data[0]
        return render_template('create_ticket.html',
                               title='Create Ticket',
                               name=user_details["firstname"]
                               )
