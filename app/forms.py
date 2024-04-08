# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf.file import FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[InputRequired(), Length(max=500)])
    poster = FileField('Poster', validators=[InputRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])