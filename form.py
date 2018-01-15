from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField
from wtforms.validators import DataRequired, Optional
class Loginform(FlaskForm):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    surname = StringField('surname', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    MiddleName= StringField('MiddleName', validators=[Optional()])
    birthPlace = StringField('birthPlace', validators=[DataRequired()])
    passport = StringField('passport', validators=[DataRequired()])

