from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index = True, unique = True)

    def __init__(self, username, password,email):
        self.username = username;
        self.password = password;
        self.email = email;