


from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from app.models import Details

class AddDetailForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email Address', validators = [DataRequired(), Email()])
    submit = SubmitField()

    def validate_email(form, field):
        email = Details.query.filter_by(email_address=field.data).first()
        if email:
            raise ValidationError('That email address has already been registered')
     
        return True