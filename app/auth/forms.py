from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import InputRequired


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[InputRequired()])
    email = StringField('email',validators=[InputRequired()])
    password = StringField('password',validators=[InputRequired()])
    con_password = StringField('confirm password',validators=[InputRequired()])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    email = StringField('email',validators=[InputRequired()])
    password = StringField('password',validators=[InputRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('submit')