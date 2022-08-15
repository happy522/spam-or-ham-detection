from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class PredictForm(FlaskForm):
    newz = StringField(label="news", validators=[ DataRequired() ])
    submit = SubmitField(label="Submit")
