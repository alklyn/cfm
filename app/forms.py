"""
All the forms used in the project are defined here.
"""
from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField, SelectField
from wtforms.validators import Required

class LoginForm(Form):
    """ Handle login """
    username = TextField('username',
                         validators=[Required()],
                         render_kw={"placeholder": "username"})

    password = PasswordField('password',
                             validators=[Required()],
                             render_kw={"placeholder": "password"})
    submit = SubmitField("sign in")


class CreateTicketForm(Form):
    """ Form for creating new tickets """
    caller = TextField('caller',
                       validators=[Required()],
                       render_kw={"placeholder": "Name of caller"})

    phone_number = TextField('phone number',
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

    villages = []
    village = SelectField('village',
                          validators=[Required()],
                          choices=villages)

    wards = []
    ward = SelectField('ward',
                       validators=[Required()],
                       choices=wards)

    partners = []
    partner = SelectField('partner',
                          validators=[Required()],
                          choices=partners)

    programmes = []
    programme = SelectField('programme',
                            validators=[Required()],
                            choices=programmes)

    topics = []
    topic = SelectField('topic',
                        validators=[Required()],
                        choices=topics)

    prioritys = []
    priority = SelectField('priority',
                           validators=[Required()],
                           choices=prioritys)

    #staffmember assigned ticket
    agents = []
    agent = SelectField('agent',
                        validators=[Required()],
                        choices=agents)

    details = TextField('details',
                        validators=[Required()],
                        render_kw={"placeholder": "query/complaint"})

    submit_button = SubmitField('submit')
