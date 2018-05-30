from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,  PasswordField
from wtforms.validators import DataRequired, Optional
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateTimeField
from datetime import datetime
class Loginform(FlaskForm):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('username',)
    password = PasswordField('password' )
    email = StringField('email', )
    surname = StringField('surname' )
    name = StringField('name' )
    MiddleName= StringField('middleName')
    birthPlace = StringField('birthPlace')
    passport = StringField('passport')


class OrderForm(FlaskForm):
    district_name = StringField('District')
    hospital_name = StringField('Hospital')
    department_name =StringField('Department')
    doctors_name = StringField('Doctors')
    date = DateTimeField('Date',format='%Y-%m-%d %H:%M:%S')



