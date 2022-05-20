from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import InputRequired,ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[InputRequired()])
    email = StringField('email',validators=[InputRequired()])
    password = StringField('password',validators=[InputRequired()])
    con_password = StringField('confirm password',validators=[InputRequired()])
    submit = SubmitField('submit')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('email',validators=[InputRequired()])
    password = StringField('password',validators=[InputRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('submit')