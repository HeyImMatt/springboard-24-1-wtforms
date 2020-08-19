from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired(message="Pet must have a name")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[URL(message="Must be a valid URL")])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Must be between 0 and 30")])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing pets"""
    photo_url = StringField("Photo URL", validators=[URL(message="Must be a valid URL")])
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")