from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=40)])
    DOB = DateField('Date of Birth', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password',[DataRequired(),EqualTo('password', message='Passwords must match')])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
    bio = TextAreaField('Biography', validators=[DataRequired(), Length(min=6, max=25)])
    photo = FileField('Photo', validators=[
        FileAllowed(['jpg','png','Images only'])
    ])
#class ProfileForm(Form):


class LoginForm(Form):
    email = TextField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

class CommentForm(Form):
    content = TextField('Comment', [DataRequired()])
    date = DateField('DateMade', validators=[DataRequired()])
    
class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class AdminUForm(Form):
    uname = TextField('Generate User Report: ', [DataRequired()])
