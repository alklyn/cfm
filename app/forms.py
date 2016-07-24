"""
All the forms used in the project are defined here.
"""
from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField, SelectField, \
                    TextAreaField, validators
from wtforms.validators import Required
from app.dbi import prep_select

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
    caller_firstname = TextField('First name of caller',
                                 validators=[Required()],
                                 render_kw={"placeholder": "Name of caller"})

    caller_lastname = TextField('Last name of caller',
                                validators=[Required()],
                                render_kw={"placeholder": "Surname of caller"})

    phone_number = TextField('Phone Number',
                             validators=[Required()],
                             render_kw={"placeholder": "Phone No of caller"})

    genders = prep_select("gender")  #list of id, gender tuples
    gender = SelectField('Gender',
                         validators=[Required()],
                         choices=genders)

    provinces = prep_select("province")  #list of id, province tuples
    province = SelectField('Province',
                           validators=[Required()],
                           choices=provinces)

    districts = prep_select("district")  #list of id, district tuples
    district = SelectField('District',
                           validators=[Required()],
                           choices=districts)

    wards = []
    ward = SelectField('Ward',
                       validators=[Required()],
                       choices=wards)

    villages = []
    village = SelectField('Village',
                          validators=[Required()],
                          choices=villages)

    wards = []
    ward = SelectField('Ward',
                       validators=[Required()],
                       choices=wards)

    partners = prep_select("partner")  #list of id, partner tuples
    partner = SelectField('Cooperating Partner',
                          validators=[Required()],
                          choices=partners)

    programmes = prep_select("programme")  #list of id, programme tuples
    programme = SelectField('Programme',
                            validators=[Required()],
                            choices=programmes)

    topics = prep_select("topic")  #list of id, topic tuples
    topic = SelectField('Help Topic',
                        validators=[Required()],
                        choices=topics)

    prioritys = prep_select("priority")  #list of id, priority tuples
    priority = SelectField('Priority',
                           validators=[Required()],
                           choices=prioritys)

    #staffmember assigned ticket
    agents = prep_select("user")  #list of id, fullname tuples
    agent = SelectField('Assign to',
                        validators=[Required()],
                        choices=agents)

    details = TextAreaField('Issue Details',
                            [validators.required()],
                            render_kw={"placeholder": "query/complaint"})

    submit = SubmitField('submit')
