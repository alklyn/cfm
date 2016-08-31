""" All the views in the the app are here """
from flask import render_template, flash, redirect, request, url_for, session
from wtforms.validators import Required
from werkzeug.exceptions import HTTPException
from app import app
from app.dbi_read import prep_select, get_tickets, get_user_details, \
    check_pw, get_ticket_updates
from app.dbi_write import add_ticket, add_update
from app.dbi import update_table, fetch_from_table
from app.forms import LoginForm, TicketForm, UpdateTicketForm
from app.validate import update_selectors, update_reassign_selector
from app.util import Pagination

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


@app.route('/logout', methods=["GET", "POST"])
def logout():
    """
    Handles user logout
    """
    del session['id']
    message = "You've successfully logged out."
    flash(message)
    return redirect(url_for('login'))


def is_logged_in():
    """
    Check if the user is logged in.
    Return True is user is logged in else return False.
    """
    try:  #Test if user is logged in
        session["id"]
    except (AttributeError, NameError, HTTPException, KeyError) as error:
        print(str(error))
        message = "Please sign in."
        flash(message, "warning")
        return False
    else:
        return True

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
            user_data = fetch_from_table(
                where_clause="username = %s",
                params=(username, ),
                table='user')
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
    if not is_logged_in():
        return redirect(url_for('login'))

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
    if not is_logged_in():
        return redirect(url_for('login'))

    userid = session["id"]
    data = get_user_details(where_clause="id = %s", params=(userid, ))
    user_details = data[0]
    return render_template('test.html',
                           title='Test Page',
                           name=user_details["firstname"],
                           lastname=user_details["lastname"],
                           username=user_details["username"])


@app.route('/index/')
def index():
    """Another test view.
    To be removed in production system
    """
    if not is_logged_in():
        return redirect(url_for('login'))

    userid = session["id"]
    data = get_user_details(where_clause="id = %s", params=(userid, ))
    user_details = data[0]
    return render_template('index.html',
                           title='Home',
                           user_details=user_details)


@app.route('/tickets/')
@app.route('/tickets/<status>')
def tickets(status='open'):
    """ Home page

    input
    =====
    status:
        open: Display only open tickets.
        closed: Display only closed tickets.
        all: Display all tickets.
    Output
        display_all: boolean
            Determines whether all the columns are shown or not
    """
    if not is_logged_in():
        return redirect(url_for('login'))

    #CSS class for each of the links (open, closed, all)
    classes = {"open": "", "closed": "", "all": ""}
    where_clause="status_id = %s"
    if status == "open":
        t_status = 1
        classes["open"] = "class=active"
    elif status == "closed":
        t_status = 2
        classes["closed"] = "class=active"
    else:
        classes["all"] = "class=active"
        t_status = 1
        where_clause="%s"

    params = (t_status, )

    tickets = get_tickets(where_clause=where_clause ,params=params)
    userid = session["id"]
    user_details = get_user_details(
        where_clause="id = %s",
        params=(userid, ),
        log_query=True)

    if user_details:
        user_data=user_details[0]
    else:
        message = "Error! Please contact IT."
        flash(message)
        return redirect(url_for('index'))


    return render_template('tickets.html',
                           title='Home',
                           user_details=user_data,
                           tickets=tickets,
                           display_all=False,
                           classes=classes)


@app.route('/create_ticket', methods=["GET", "POST"])
def create_ticket():
    """ page for creating new tickets

    """
    if not is_logged_in():
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
    if not is_logged_in():
        return redirect(url_for('login'))

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

    except (AttributeError, NameError, HTTPException, KeyError) as error:
        message = "Error proceccing request."
    else:
        userid = session["id"]
        message = "Ticket successfully saved."
        data = get_user_details(where_clause="id = %s", params=(userid, ))
        user_details = data[0]

    flash(message)
    return redirect(url_for('index'))


@app.route('/update_ticket', methods=["POST", "GET"])
@app.route('/update_ticket/<ticket_number>', methods=["POST", "GET"])
def update_ticket(ticket_number):
    """ Update a ticket """
    if not is_logged_in():
        return redirect(url_for('login'))

    ticket_id = int(ticket_number)
    tickets = get_tickets(where_clause="a.id = %s", params=(ticket_id, ))
    if tickets:
        ticket = tickets[0]
    else:
        message = "Failed to retreive ticket. Please contact IT."
        flash(message)
        return redirect(url_for('index'))

    ticket_updates = get_ticket_updates(
        where_clause="a.ticket_id = %s",
        params=(ticket_id, ))

    userid = session["id"]
    user_details = \
        fetch_from_table(where_clause="id = %s", params=(userid, ))[0]

    if request.method == "POST":
        form, reassign_set = update_reassign_selector()
    else:
        form = UpdateTicketForm()
        reassign_set = False

    session["ticket_id"] = ticket_id
    return render_template('update_ticket.html',
                           title='Update Ticket',
                           user_details=user_details,
                           ticket=ticket,
                           form=form,
                           reassign_set=reassign_set,
                           ticket_updates=ticket_updates)


@app.route('/save_ticket_update', methods=["POST"])
def save_ticket_update():
    """Save update to a ticket.
    Will need to refactor this function. It's too big
    There are 3 possible update types.
        1. Normal update to a ticket.
        2. Close ticket.
        3. Reassign ticket to a different agent.
    """
    if not is_logged_in():
        return redirect(url_for('login'))

    try:
        update_type = request.form["update_type"]
        if update_type == "3" :
            #Re-assign Ticket
            new_agent_id = int(request.form["reassign_ticket"])
        else:
            details = request.form["update_details"]

    except (AttributeError, NameError, HTTPException, KeyError) as error:
        message = str(error)
        #message = "Error. Please contact IT."
        flash(message)
        return redirect(url_for('index'))

    userid = session["id"]
    message = "Update successfully posted."
    data = get_user_details(where_clause="id = %s", params=(userid, ))
    user_details = data[0]

    if update_type == "1":
        pass  #Nothig to do here yet!
    elif update_type == "2":
        #Close the ticket
        #update_table(table="", set_string="", data=(), where_string="")
        set_string = "status_id = %s"  #Corresponds to ticket closed
        data = (2, session["ticket_id"])
        where_string = "id = %s"
        update_table(
            table="ticket",
            set_string=set_string,
            where_string=where_string,
            data=data
            )
        message = "Ticket successfully closed."

    elif update_type == "3":
        #Re-assign the ticket
        #get_tickets(where_clause="status_id = %s", params=(1, ))
        where_clause="a.id = %s"
        params = (session["ticket_id"], )
        ticket = tickets = get_tickets(
            where_clause=where_clause,
            params=params)[0]

        agents = fetch_from_table(
                required_columns="firstname, lastname",
                where_clause="id = %s",
                params=(new_agent_id, ),
                table="user")

        if agents:
            new_agent = agents[0]
        else:
            message = "Failed to re-assign ticket. Please contact IT."
            flash(message)
            return redirect(url_for('index'))

        details = "Ticket reassigned from {} to {} {}".format(
            ticket["rep"],
            new_agent["firstname"],
            new_agent["lastname"])

        #Now changed the agent in the ticket table
        set_string = "assigned_to = %s"
        data = (new_agent_id, session["ticket_id"])
        where_string = "id = %s"
        update_table(
            table="ticket",
            set_string=set_string,
            where_string=where_string,
            data=data
            )
    else:
        #Invalid option chosen. Somehow?
        message = "Invalid option chosen. Somehow?"
        flash(message)
        return redirect(url_for('index'))

    add_update(
        update_type,
        session["ticket_id"],
        details,
        session["id"])

    flash(message)

    if update_type == "2":
        return redirect(url_for('index'))
    else:
        url = 'update_ticket/{}'.format(session["ticket_id"])
        return redirect(url)
