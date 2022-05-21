from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import InputRequired


class UpdateForm(FlaskForm):
    bio = StringField('bio',validators=[InputRequired()])
    submit = SubmitField('submit')

class BlogForm(FlaskForm):
    title = StringField('title',validators=[InputRequired()])
    description = TextAreaField('description',validators=[InputRequired()])
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    comment = StringField('comment',validators=[InputRequired()])
    submit = SubmitField('Comment')