

from app import db


class User(  db.Model):

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index = True, unique = True)




class Register( db.Model):
    reg_id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(64), index=True, unique=True)
    name  = db.Column(db.String(120), index=True, unique=True)
    MiddleName = db.Column(db.String(120), index=True, unique=True)
    birthPlace = db.Column(db.String(120), unique=True)
    passport = db.Column(db.String(120), unique=True)

class District(db.Model):
    dis_id = db.Column(db.Integer, primary_key=True)
    disName = db.column(db.String(100))
    hospitals = db.relationship('Hospital', bacref='district', lazy='dynamic')


class Hospital(db.Model):
    hos_id = db.Column(db.Integer, primary_key=True)
    hosName= db.Column(db.String(60))
    districts_id=db.Column(db.Integer, db.ForeignKey('district.id'))
    doctors = db.relationship('Doctors', bacref = 'hospital', lazy = 'dynamic')
    depHos=db.relationship('Department',secondary=table, bacref=db.backref('hospital', lazy='dynamic'))

class Department(db.Model):
    dep_id = db.Column(db.Integer, primary_key=True )
    depName= db.Column(db.String(60))
    doctors = db.relationship('Doctors', bacref='department', lazy='dynamic')



class Doctors (db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    docName= db.Column(db.String(60))
    docSurname = db.Column(db.String(60))
    dep_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    hos_id=db.Column(db.Integer, db.ForeignKey('hospital.id'))

table = db.Table('table',
        db.Column('hos_id', db.Integer, db.ForeignKey('hospital.hos_id')),
        db.Column('dep_id', db.Integer, db.ForeignKey('department.dep_id'))
                 )

def __init__(self, username, password,email):
    self.username = username;
    self.password = password;
    self.email = email;
