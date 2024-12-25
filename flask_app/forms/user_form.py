# from flask_wtf import FlaskForm
from wtforms import Form, StringField, EmailField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from dateutil.relativedelta import relativedelta
from datetime import date

def password_valid(min=-1, max=-1, message=None):
    if not message: # No message entered, so use the default in the line below
        message = 'Password must be between %d and %d characters long.' % (min, max)
    def _password_valid(form, field):
        pwd_input : str = field.data
        l = pwd_input and len(pwd_input) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
        has_lower_case_letter = False
        has_upper_case_letter = False
        has_digit = False
        has_no_spaces = True
        for cur_char in pwd_input:
            if not has_digit and cur_char.isnumeric():
                has_digit = True
            elif has_no_spaces and cur_char == " ":
                has_no_spaces = False
                break # Exit early - password is automatically invalid
            elif not has_lower_case_letter and cur_char.islower() and cur_char.isalpha():
                has_lower_case_letter = True
            elif not has_upper_case_letter and cur_char.isupper() and cur_char.isalpha():
                has_upper_case_letter = True
        if has_lower_case_letter and has_upper_case_letter and has_digit and has_no_spaces == False:
            raise ValidationError(f"Password must contain at least one lower-case letter, at least" +
                "upper-case letter, at least one digit, no spaces, and must be {min} through {max} characters in length.")
    return _password_valid

def is_old_enough(message = None):
    if not message:
        message = "You must be 18 years of age or older!"
    def _is_old_enough(form, field):
        date_input = date.fromisoformat(field.data)
        if date_input > date.today()+relativedelta(years=-18): # Validate if user is 18 or older
            raise ValidationError(message)
    return _is_old_enough

class UserForm(Form):
    first_name = StringField("first_name",[
        DataRequired(message="Please enter your first name!"),
        Length(min=2, max=255, message="First name must be 2 through 255 characters, inclusively.")])
    last_name = StringField("last_name",[
        DataRequired(message="Please enter your last name!"),
        Length(min=2, max=255, message="Last name must be 2 through 255 characters, inclusively.")])
    username = StringField("username",[
        DataRequired(message="Please enter the username you want."),
        Length(min=2, max=255, message="Username must be 2 through 255 characters, inclusively.")])
    birthdate = DateField("birthdate",[
        DataRequired(message="Please enter your birth date."),
        is_old_enough()
        ])
    email = EmailField("email",[
        DataRequired(message="Please enter the email you will use."),
        Length(min=5, max=255, message="Email must be 5 through 255 characters, inclusively."),
        Email(message="Please enter a valid email.")])
    password = PasswordField("password",[
        DataRequired(message="Please enter your password!"),
        EqualTo("confirmed_password",message="Your passwords must agree."),
        password_valid(8,30)
    ])
    confirmed_password = PasswordField("confirmed_password", [
        DataRequired(message="Please confirm your password!"),
    ])
    # submit = SubmitField("Add author")