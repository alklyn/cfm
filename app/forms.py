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
                         render_kw={"placeholder": "username"})

    password = PasswordField('password',
                             validators=[InputRequired()],
                             render_kw={"placeholder": "password"})
    submit = SubmitField("sign in")


class CreateTicketForm(Form):
    """ Form for creating new tickets """
    caller_firstname = TextField('First name of caller',
                                 validators=[InputRequired()],
                                 render_kw={"placeholder": "Name of caller"})

    caller_lastname = TextField('Last name of caller',
                                validators=[InputRequired()],
                                render_kw={"placeholder": "Surname of caller"})

    phone_number = TextField('Phone Number',
                             validators=[InputRequired()],
                             render_kw={"placeholder": "Phone No of caller"})

    genders = prep_select("gender")  #list of id, gender tuples
    gender = SelectField('Gender',
                         validators=[InputRequired()],
                         choices=genders)

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
                       render_kw={"onchange": "this.form.submit()"})

    villages = []
    village = SelectField('Village',
                          validators=[InputRequired()],
                          choices=villages)

    partners = prep_select("partner")  #list of id, partner tuples
    partner = SelectField('Cooperating Partner',
                          validators=[InputRequired()],
                          choices=partners)

    programmes = prep_select("programme")  #list of id, programme tuples
    programme = SelectField('Programme',
                            validators=[InputRequired()],
                            choices=programmes)

    topics = prep_select("topic")  #list of id, topic tuples
    topic = SelectField('Help Topic',
                        validators=[InputRequired()],
                        choices=topics)

    prioritys = prep_select("priority")  #list of id, priority tuples
    priority = SelectField('Priority',
                           validators=[InputRequired()],
                           choices=prioritys)

    #staffmember assigned ticket
    agents = prep_select("user")  #list of id, fullname tuples
    agent = SelectField('Assign to',
                        validators=[InputRequired()],
                        choices=agents)

    details = TextAreaField('Issue Details',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "query/complaint"})

    open_ticket = SubmitField('Create ticket')
