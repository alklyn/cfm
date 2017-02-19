"""
All the forms used in the project are defined here.
"""
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, PasswordField, SelectField, \
                    TextAreaField, IntegerField, RadioField, validators
from wtforms.validators import Required, InputRequired
from app.dbi_read import prep_select

class LoginForm(FlaskForm):
    """ Handle login """
    username = TextField(
        'username',
        validators=[InputRequired()],
        render_kw={"placeholder": "username",
            "class": "ticket_element"})

    password = PasswordField(
                'password',
                validators=[InputRequired()],
                render_kw={"placeholder": "password",
                           "class": "ticket_element"})
    submit = SubmitField("sign in")


class TicketForm(FlaskForm):
    """ FlaskForm for creating new tickets """
    caller_firstname = TextField(
        'First name of caller',
        validators=[InputRequired()],
        render_kw={
            "placeholder": "Name of caller",
            "class": "ticket_element",
            "onKeyUp": "processInput(this)"})

    caller_lastname = TextField(
        'Last name of caller',
        validators=[InputRequired()],
        render_kw={
            "placeholder": "Surname of caller",
            "class": "ticket_element",
            "onKeyUp": "processInput(this)"})

    phone_number = IntegerField(
        'Phone No',
        validators=[InputRequired()],
        render_kw={
            "placeholder": "777777777",
            "class": "ticket_element",
            "onKeyUp": "processInput(this)"})

    genders = prep_select("gender")  #list of id, gender tuples
    gender = SelectField(
        'Gender',
        validators=[InputRequired()],
        choices=genders,
        render_kw={
            "class": "ticket_element",
            "onChange": "processInput(this)"})

    provinces = prep_select("province")  #list of id, province tuples
    province = SelectField(
        'Province',
        validators=[InputRequired()],
        choices=provinces,
        render_kw={"onChange": "processInput(this)"})

    districts = []  #list of id, district tuples
    district = SelectField(
        'District',
        validators=[InputRequired()],
        choices=districts,
        render_kw={"onchange": "processInput(this)"})

    wards = []
    ward = SelectField('Ward',
        validators=[InputRequired()],
        choices=wards,
        render_kw={"onchange": "processInput(this)",
            "class": "ticket_element"})

    villages = []
    village = TextField('Village',
        validators=[InputRequired()],
        render_kw={"class": "ticket_element",
            "placeholder": "Village name",
            "onKeyUp": "processInput(this)"})


    partners = prep_select("partner")  #list of id, partner tuples
    partner = SelectField(
        'Cooperating Partner',
        validators=[InputRequired()],
        choices=partners,
        render_kw={"class": "ticket_element",
            "onChange": "processInput(this)"})

    programmes = prep_select("programme")  #list of id, programme tuples
    programme = SelectField(
        'Programme',
        validators=[InputRequired()],
        choices=programmes,
        render_kw={"class": "ticket_element",
            "onChange": "processInput(this)"})

    topics = prep_select("topic")  #list of id, topic tuples
    topic = SelectField(
        'Help Topic',
        validators=[InputRequired()],
        choices=topics,
        render_kw={"class": "ticket_element",
            "onChange": "processInput(this)"})

    prioritys = prep_select("priority")  #list of id, priority tuples
    priority = SelectField(
        'Priority',
        validators=[InputRequired()],
        choices=prioritys,
        render_kw={"class": "ticket_element",
            "onChange": "processInput(this)"})

    #staffmember assigned ticket
    #list of id, fullname tuples
    agents = prep_select( table="agent", where_clause="id != %s", params=(1, ))
    agent = SelectField('Assign to',
        validators=[InputRequired()],
        choices=agents,
        render_kw={"class": "ticket_element",
        "onChange": "processInput(this)"})

    details = TextAreaField(
        'Issue Details',
        [validators.InputRequired()],
        render_kw={"placeholder": "query/complaint",
        "class": "ticket_element",
        "onKeyUp": "processInput(this)"})

    open_ticket = SubmitField(
        'Open ticket',
        render_kw={"onClick": "processInput(this)"})


class UpdateTicketForm(FlaskForm):
    """ FlaskForm for updating tickets """
    update_types = prep_select("update_type")  #list of id, update_type tuples
    update_type = SelectField(
        'Action',
        validators=[InputRequired()],
        choices=update_types,
        render_kw={
            "class": "ticket_element",
            "onChange": "processInput(this)"})

    #staffmember to be re-assigned ticket
    agents = []  #list of id, fullname tuples
    reassign_ticket = SelectField('Re-assign to',
        validators=[InputRequired()],
        choices=agents,
        render_kw={"class": "ticket_element",
        "onChange": "processInput(this)"})

    update_details = TextAreaField(
        'Update',
        validators=[InputRequired()],
        render_kw={
            "placeholder": "",
            "class": "ticket_element",
            "onKeyUp": "processInput(this)"})

    submit_button = SubmitField(
        'Update ticket',
        render_kw={"onClick": "processInput(this)"})
