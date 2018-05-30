from flask_login import UserMixin

from app import db
from flask_admin.contrib.sqla import ModelView
from app import admin
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm




class Register(UserMixin,  db.Model):
    reg_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(120), index=True, unique=True)
    email= db.Column(db.String(60), index=True, unique=True)
    surname = db.Column(db.String(64), index=True, unique=True)
    name  = db.Column(db.String(120), index=True, unique=True)
    MiddleName = db.Column(db.String(120), index=True, unique=True)
    birthPlace = db.Column(db.String(120), unique=True)
    passport = db.Column(db.String(120), unique=True)

    def get_id(self):
        return (self.reg_id)

class District(db.Model):
    dis_id = db.Column(db.Integer, primary_key=True)
    disName = db.Column(db.String(100))
    hospitals = db.relationship('Hospital', backref='district', lazy='dynamic')
    def __repr__(self):
        return "{}.".format(self.disName)


class Hospital(db.Model):
    hos_id = db.Column(db.Integer, primary_key=True)
    hosName= db.Column(db.String(60))
    districts_id=db.Column(db.Integer, db.ForeignKey('district.dis_id'))
    departments = db.relationship('Department', backref = 'hospital', lazy = 'dynamic')
    doctors=db.relationship('Doctors', backref='hospital', lazy='dynamic')


    def __repr__(self):
        return "{}." .format( self.hosName)

class Department(db.Model):
    dep_id = db.Column(db.Integer, primary_key=True )
    depName= db.Column(db.String(60))
    doctors = db.relationship('Doctors', backref='department', lazy='dynamic')
    hospitals_id=db.Column(db.Integer, db.ForeignKey('hospital.hos_id'))

    def __repr__(self):
        return "{}.".format(self.depName)


class Doctors (db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    docName= db.Column(db.String(60))
    docSurname = db.Column(db.String(60))
    dep_id = db.Column(db.Integer, db.ForeignKey('department.dep_id'))
    hos_id=db.Column(db.Integer, db.ForeignKey('hospital.hos_id'))


    def __repr__(self):
        return "{} {}".format(self.docName, self.docSurname)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    district_name=db.Column(db.String(100))
    hospital_name=db.Column(db.String(100))
    department_name=db.Column(db.String(100))
    doctors_name=db.Column(db.String(100))
    date=db.Column(db.DateTime, nullable=False)
def district():
    return District.query
def hospital():
    return Hospital.query
def department():
    return Department.query
def doctors():
    return Doctors.query
def time():
    return Order.query

def register():
    return Register.query
class Queue(FlaskForm):
    dis=QuerySelectField(query_factory=district, allow_blank=False)
    hos= QuerySelectField(query_factory=hospital, allow_blank=False)
    dep=QuerySelectField(query_factory=department, allow_blank=False)
    doc= QuerySelectField(query_factory=doctors, allow_blank=False)
    time = QuerySelectField(query_factory=time, allow_blank=False)




admin.add_view(ModelView(Register, db.session))
admin.add_view(ModelView(District, db.session))
admin.add_view(ModelView(Hospital, db.session))
admin.add_view(ModelView(Department, db.session))
admin.add_view(ModelView(Doctors, db.session))
admin.add_view(ModelView(Order, db.session))