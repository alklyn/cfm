""" All the views in the the app are here """
from flask import render_template, flash, redirect, request, url_for, session
from wtforms import TextField, SubmitField, PasswordField, SelectField, \
                    TextAreaField, validators
from wtforms.validators import Required
from werkzeug.exceptions import HTTPException
from app import app
from app import dbi
from app.dbi import prep_select, add_ticket
from app.forms import LoginForm, TicketForm
from app.validate import update_selectors


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
                           form=form)


@app.route('/validate_login', methods=['POST'])
def validate_login():
    """ Check if user provided correct password. """
    try:
        username = request.form['username']
        password = request.form['password']
    except NameError as error:
        message = str(error)
    else:
        if dbi.check_pw(username, password):
            #get_user_details(required_columns="*", where_clause="%s", params=(1, )
            user_data = dbi.get_user_details(where_clause="username = %s",
                                             params=(username, ))
            session["id"] = user_data[0]["id"]
            return redirect(url_for('index'))
        else:
            message = "Access Denied!"
    flash(message, "error")
    return redirect(url_for('login'))


@app.route('/users/')
@app.route('/users/<username>')
def users(username='all'):
    """Test view.
    To be removed in production system
    """
    if username == 'all':
        where_clause = "%s"
        params = (1, )
    else:
        where_clause = "username = %s"
        params = (username, )
    user_details = dbi.get_user_details(where_clause=where_clause,
                                        params=params)
    return render_template('users.html',
                           title='Users',
                           user_details=user_details)


@app.route('/test/')
def test():
    """Another test view.
    To be removed in production system
    """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('index'))
    else:
        userid = session["id"]
        data = dbi.get_user_details(where_clause="id = %s", params=(userid, ))
        user_details = data[0]
        return render_template('test.html',
                               title='Test Page',
                               name=user_details["firstname"],
                               lastname=user_details["lastname"],
                               username=user_details["username"])


@app.route('/index')
def index():
    """ Home page """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))
    else:
        userid = session["id"]
        data = dbi.get_user_details(where_clause="id = %s", params=(userid, ))
        user_details = data[0]
        return render_template('index.html',
                               title='Home',
                               name=user_details["firstname"])


@app.route('/create_ticket', methods=["GET", "POST"])
def create_ticket():
    """ page for creating new tickets

    """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))

    if request.method == "POST":
        form, province_set, district_set, ward_set, topic_set = \
        update_selectors()
    else:
        form = TicketForm()
        province_set = False
        district_set = False
        ward_set = False
        topic_set = False

    userid = session["id"]
    data = dbi.get_user_details(where_clause="id = %s", params=(userid, ))
    user_details = data[0]

    # if 'message' in locals():
    #     flash(message, "error")
    country_code = "+263"
    return render_template('create_ticket.html',
                           title='Create Ticket',
                           name=user_details["firstname"],
                           form=form,
                           province_set=province_set,
                           district_set=district_set,
                           ward_set=ward_set,
                           country_code=country_code)


@app.route('/save_ticket', methods=["POST"])
def save_ticket():
    """Save new tickets

    """
    try:
        caller_firstname = request.form["caller_firstname"]
        caller_lastname = request.form["caller_lastname"]
        phone_number = request.form["phone_number"]
        gender_id = request.form["gender"]
        location_id = request.form["village"]
        topic_id = request.form["topic"]
        priority_id = request.form["priority"]
        partner_id = request.form["partner"]
        programme_id = request.form["programme"]
        details = request.form["details"]
        created_by = session["id"]
        assigned_to = request.form["agent"]
    except (AttributeError, NameError, HTTPException) as error:
        message = str(error)
    else:
        add_ticket(
                   caller_firstname, caller_lastname, phone_number, gender_id,
                   location_id, topic_id, priority_id, partner_id,
                   programme_id, details, created_by, assigned_to)
        userid = session["id"]
        massage = "Ticket successfully saved."
        data = dbi.get_user_details(where_clause="id = %s", params=(userid, ))
        user_details = data[0]
    return render_template('index.html',
                           title='Home',
                           name=user_details["firstname"])
