""" All the views in the the app are here """
from flask import render_template, flash, redirect, request, url_for, session
from wtforms.validators import Required
from werkzeug.exceptions import HTTPException
from app import app
from app.dbi import prep_select, add_ticket, get_tickets, get_user_details, \
    check_pw
from app.forms import LoginForm, TicketForm, UpdateTicketForm
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
        if check_pw(username, password):
            #get_user_details(required_columns="*", where_clause="%s", params=(1, )
            user_data = get_user_details(where_clause="username = %s",
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
    user_details = get_user_details(where_clause=where_clause,
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
        data = get_user_details(where_clause="id = %s", params=(userid, ))
        user_details = data[0]
        return render_template('test.html',
                               title='Test Page',
                               name=user_details["firstname"],
                               lastname=user_details["lastname"],
                               username=user_details["username"])


@app.route('/index')
def index():
    """ Home page

    Output
        display_all: boolean
            Determines whether all the columns are shown or not
    """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))
    else:
        tickets = get_tickets()
        userid = session["id"]
        user_details = \
            get_user_details(where_clause="id = %s", params=(userid, ))[0]

        #Determines how much info is displayed in the table

        return render_template('index.html',
                               title='Home',
                               user_details=user_details,
                               tickets=tickets,
                               display_all=False)


@app.route('/create_ticket', methods=["GET", "POST"])
def create_ticket():
    """ page for creating new tickets

    """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))

    if request.method == "POST":
        form, province_set, district_set, ward_set = \
        update_selectors()
    else:
        form = TicketForm()
        province_set = False
        district_set = False
        ward_set = False

    userid = session["id"]
    user_details = \
        get_user_details(where_clause="id = %s", params=(userid, ))[0]

    # if 'message' in locals():
    #     flash(message, "error")
    country_code = "+263"
    return render_template('create_ticket.html',
                           title='Create Ticket',
                           user_details=user_details,
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
        country_code = "+263"
        phone_number = country_code + request.form["phone_number"]

        add_ticket(
            request.form["caller_firstname"],
            request.form["caller_lastname"],
            phone_number,
            request.form["gender"],
            request.form["ward"],
            request.form["village"],
            request.form["topic"],
            request.form["priority"],
            request.form["partner"],
            request.form["programme"],
            request.form["details"],
            session["id"],
            request.form["agent"])

    except (AttributeError, NameError, HTTPException) as error:
        message = str(error)
    else:
        userid = session["id"]
        message = "Ticket successfully saved."
        data = get_user_details(where_clause="id = %s", params=(userid, ))
        user_details = data[0]

    flash(message)
    return redirect(url_for('index'))


@app.route('/update_ticket/<ticket_number>')
def update_ticket(ticket_number):
    """ Update a ticket """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))
    else:
        ticket_id = int(ticket_number)
        ticket = get_tickets(where_clause="a.id = %s", params=(ticket_id, ))[0]
        userid = session["id"]
        user_details = \
            get_user_details(where_clause="id = %s", params=(userid, ))[0]

    form = UpdateTicketForm()
    return render_template('update_ticket.html',
                           title='Update Ticket',
                           user_details=user_details,
                           ticket=ticket,
                           form=form)
