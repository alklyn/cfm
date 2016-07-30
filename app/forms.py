"""
All the forms used in the project are defined here.
"""
from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField, SelectField, \
                    TextAreaField, validators
from wtforms.validators import Required, InputRequired
from app.dbi import prep_select

class LoginForm(Form):
    """ Handle login """
    username = TextField('username',
                         validators=[InputRequired()],
                         render_kw={"placeholder": "username",
                                    "class": "ticket_element"})

    password = PasswordField('password',
                             validators=[InputRequired()],
                             render_kw={"placeholder": "password",
                                        "class": "ticket_element"})
    submit = SubmitField("sign in")


class CreateTicketForm(Form):
    """ Form for creating new tickets """
    caller_firstname = TextField('First name of caller',
                                 validators=[InputRequired()],
                                 render_kw={"placeholder": "Name of caller",
                                            "class": "ticket_element"})

    caller_lastname = TextField('Last name of caller',
                                validators=[InputRequired()],
                                render_kw={"placeholder": "Surname of caller",
                                           "class": "ticket_element"})

    phone_number = TextField('Phone Number',
                             validators=[InputRequired()],
                             render_kw={"placeholder": "Phone No of caller",
                                        "class": "ticket_element"})

    genders = prep_select("gender")  #list of id, gender tuples
    gender = SelectField('Gender',
                         validators=[InputRequired()],
                         choices=genders,
                         render_kw={"class": "ticket_element"})

    provinces = prep_select("province")  #list of id, province tuples
    province = SelectField('Province',
                           validators=[InputRequired()],
                           choices=provinces,
                           render_kw={"onchange": "this.form.submit()"})

    districts = []  #list of id, district tuples
    district = SelectField('District',
                           validators=[InputRequired()],
                           choices=districts,
                           render_kw={"onchange": "this.form.submit()"})

    wards = []
    ward = SelectField('Ward',
                       validators=[InputRequired()],
                       choices=wards,
                       render_kw={"onchange": "this.form.submit()",
                                  "class": "ticket_element"})

    villages = []
    village = SelectField('Village',
                          validators=[InputRequired()],
                          choices=villages,
                          render_kw={"class": "ticket_element"})


    partners = prep_select("partner")  #list of id, partner tuples
    partner = SelectField('Cooperating Partner',
                          validators=[InputRequired()],
                          choices=partners,
                          render_kw={"class": "ticket_element"})

    programmes = prep_select("programme")  #list of id, programme tuples
    programme = SelectField('Programme',
                            validators=[InputRequired()],
                            choices=programmes,
                            render_kw={"class": "ticket_element"})

    topics = prep_select("topic")  #list of id, topic tuples
    topic = SelectField('Help Topic',
                        validators=[InputRequired()],
                        choices=topics,
                        render_kw={"class": "ticket_element"})

    prioritys = prep_select("priority")  #list of id, priority tuples
    priority = SelectField('Priority',
                           validators=[InputRequired()],
                           choices=prioritys,
                           render_kw={"class": "ticket_element"})

    #staffmember assigned ticket
    agents = prep_select("user")  #list of id, fullname tuples
    agent = SelectField('Assign to',
                        validators=[InputRequired()],
                        choices=agents,
                        render_kw={"class": "ticket_element"})

    details = TextAreaField('Issue Details',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "query/complaint",
                                       "class": "ticket_element",
                                       "onKeyUp": "updateOpenDiv(this.id)"})

    open_ticket = SubmitField('Open ticket')
