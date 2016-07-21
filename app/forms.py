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
    caller = TextField('Caller',
                       validators=[Required()],
                       render_kw={"placeholder": "Name of caller"})

    phone_number = TextField('Phone Number',
                             validators=[Required()],
                             render_kw={"placeholder": "Phone No of caller"})

    genders = []
    gender = SelectField('Gender',
                         validators=[Required()],
                         choices=genders)

    provinces = []
    province = SelectField('Province',
                           validators=[Required()],
                           choices=provinces)

    villages = []
    village = SelectField('Village',
                          validators=[Required()],
                          choices=villages)

    wards = []
    ward = SelectField('Ward',
                       validators=[Required()],
                       choices=wards)

    partners = []
    partner = SelectField('partner',
                          validators=[Required()],
                          choices=partners)

    programmes = []
    programme = SelectField('Programme',
                            validators=[Required()],
                            choices=programmes)

    topics = []
    topic = SelectField('Help Topic',
                        validators=[Required()],
                        choices=topics)

    prioritys = []
    priority = SelectField('Priority',
                           validators=[Required()],
                           choices=prioritys)

    #staffmember assigned ticket
    agents = []
    agent = SelectField('Assign to',
                        validators=[Required()],
                        choices=agents)

    details = TextField('Issue Details',
                        validators=[Required()],
                        render_kw={"placeholder": "query/complaint"})

    submit = SubmitField('submit')
