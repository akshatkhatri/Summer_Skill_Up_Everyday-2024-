from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,Email
# from form import LoginForm

class Loginform(FlaskForm):
    email = StringField("email",validators = [InputRequired(message = "Please enter Email"),Email(message = "Please enter valid email address")])
    password = PasswordField("Password",validators = [InputRequired(message = "Please Enter your Password")])
    submit = SubmitField("login")
    
    