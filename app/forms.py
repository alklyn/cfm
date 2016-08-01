"""
All the forms used in the project are defined here.
"""
from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField, SelectField, \
                    TextAreaField, IntegerField, validators
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


class TicketForm(Form):
    """ Form for creating new tickets """
    caller_firstname = TextField('First name of caller',
                                 validators=[InputRequired()],
                                 render_kw={"placeholder": "Name of caller",
                                            "class": "ticket_element",
                                            "onKeyUp": "processInput(this.id, this.form)"})

    caller_lastname = TextField('Last name of caller',
                                validators=[InputRequired()],
                                render_kw={"placeholder": "Surname of caller",
                                           "class": "ticket_element",
                                           "onKeyUp": "processInput(this.id, this.form)"})

    phone_number = IntegerField('Phone No',
                             validators=[InputRequired()],
                             render_kw={"placeholder": "777777777",
                                        "class": "ticket_element",
                                        "onKeyUp": "processInput(this.id, this.form)"})

    genders = prep_select("gender")  #list of id, gender tuples
    gender = SelectField('Gender',
                         validators=[InputRequired()],
                         choices=genders,
                         render_kw={"class": "ticket_element",
                         "onChange": "processInput(this.id, this.form)"})

    provinces = prep_select("province")  #list of id, province tuples
    province = SelectField('Province',
                           validators=[InputRequired()],
                           choices=provinces,
                           render_kw={"onChange": "processInput(this.id, this.form)"})

    districts = []  #list of id, district tuples
    district = SelectField('District',
                           validators=[InputRequired()],
                           choices=districts,
                           render_kw={"onchange": "processInput(this.id, this.form)"})

    wards = []
    ward = SelectField('Ward',
                       validators=[InputRequired()],
                       choices=wards,
                       render_kw={"onchange": "processInput(this.id, this.form)",
                                  "class": "ticket_element"})

    villages = []
    village = SelectField('Village',
                          validators=[InputRequired()],
                          choices=villages,
                          render_kw={"class": "ticket_element",
                                     "onChange": "processInput(this.id, this.form)"})


    partners = prep_select("partner")  #list of id, partner tuples
    partner = SelectField('Cooperating Partner',
                          validators=[InputRequired()],
                          choices=partners,
                          render_kw={"class": "ticket_element",
                          "onChange": "processInput(this.id, this.form)"})

    programmes = prep_select("programme")  #list of id, programme tuples
    programme = SelectField('Programme',
                            validators=[InputRequired()],
                            choices=programmes,
                            render_kw={"class": "ticket_element",
                            "onChange": "processInput(this.id, this.form)"})

    topics = prep_select("topic")  #list of id, topic tuples
    topic = SelectField('Help Topic',
                        validators=[InputRequired()],
                        choices=topics,
                        render_kw={"class": "ticket_element",
                                   "onChange": "processInput(this.id, this.form)"})

    prioritys = prep_select("priority")  #list of id, priority tuples
    priority = SelectField('Priority',
                           validators=[InputRequired()],
                           choices=prioritys,
                           render_kw={"class": "ticket_element",
                           "onChange": "processInput(this.id, this.form)"})

    #staffmember assigned ticket
    agents = prep_select("user")  #list of id, fullname tuples
    agent = SelectField('Assign to',
                        validators=[InputRequired()],
                        choices=agents,
                        render_kw={"class": "ticket_element",
                        "onChange": "processInput(this.id, this.form)"})

    details = TextAreaField('Issue Details',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "query/complaint",
                                       "class": "ticket_element",
                                       "onKeyUp": "processInput(this.id)"})

    open_ticket = SubmitField('Open ticket')
