import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:tala@localhost/Med'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS =False
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS', False))
MAIL_USE_SSL = int(os.environ.get('MAIL_USE_SSL', True))
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'talgart11@gmail.com')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'talasarkeev')


ADMINS = ['talgart11@gmail.com']