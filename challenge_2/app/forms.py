
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from app.models import Details

class AddDetailForm(FlaskForm):
    # Define form fields
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email Address', validators = [DataRequired(), Email()])
    submit = SubmitField()

    # Validate the email field ensuring not duplicates
    # Flask form handles the self first argument. Beware, Linters
    def validate_email(form, field):
        email = Details.query.filter_by(email_address=field.data).first()
        if email:
            raise ValidationError('That email address has already been registered')
     
        return True