from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


class IMCForm(FlaskForm):

    altura = FloatField('altura', [DataRequired()])

    peso = FloatField('peso', [DataRequired()])

    submit = SubmitField('submit')
