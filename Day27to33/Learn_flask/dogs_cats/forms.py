from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, InputRequired,EqualTo

class LoginForm(FlaskForm):
    FullName = StringField("Full Name",validators=[InputRequired(message = "Please enter your full name")])
    email = StringField("email",validators=[InputRequired(message="please enter a email"),Email(message = "Please enter a valid email address")])
    Password = PasswordField("Password",validators=[InputRequired(message="Please enter the password")])
    Conf_Password = PasswordField("Confirm Password",validators=[InputRequired(message="Please enter confirm Password"),EqualTo("Password",message = "passwords don't match")])
    submit = SubmitField("Submit")
