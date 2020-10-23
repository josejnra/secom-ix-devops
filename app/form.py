from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):

    name = StringField('name', [
        DataRequired()])

    email = StringField('email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])

    message = StringField('message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])

    submit = SubmitField('Submit')
