""" All the views in the the app are here """
from flask import render_template, flash, redirect, request, url_for, session
from app import app
from app import dbi
from app.forms import LoginForm, CreateTicketForm


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
    """ page for creating new tickets """
    try:  #Test if user is logged in
        session["id"]
    except NameError:
        return redirect(url_for('login'))
    else:
        userid = session["id"]
        data = dbi.get_user_details(where_clause="id = %s", params=(userid, ))
        user_details = data[0]
        form = CreateTicketForm()
        return render_template('create_ticket.html',
                               title='Create Ticket',
                               name=user_details["firstname"],
                               form=form)
