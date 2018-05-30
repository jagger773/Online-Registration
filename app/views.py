from  app.form import Loginform, RegisterForm, OrderForm

from flask import request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from app.models import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, login_manager
from app.models import Register
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return Register.query.get(int(user_id))

@app.route('/contact', methods= ['GET', 'POST'])
def contact():
    form = Loginform()
    forms = OrderForm()

    if request.method =='POST' and form.validate():
        user = Register.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('zapis'))

        return "<h1>Invalid login or password</h1>"



    return render_template('contact.html', form=form, forms=forms)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post')
def post():
    return render_template('post.html')



@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = RegisterForm()

    if request.method=='POST':
        hashed_password= generate_password_hash(form.password.data, method="sha256")
        user = Register(username = form.username.data, password=hashed_password,
                        email = form.email.data,
                        surname = form.surname.data,
                        name=form.name.data,        MiddleName=form.MiddleName.data,
                        birthPlace=form.birthPlace.data,
                        passport=form.passport.data
                        )
        db.session.add(user)
        db.session.commit()
        return render_template('contact.html', form=form)
    return render_template('signup.html', form=form)




@app.route('/zapis', methods=['GET', 'POST'])
def zapis():
    forms=OrderForm()
    if request.method=='POST':
        user = Order(district_name=forms.district_name.data, hospital_name=forms.hospital_name.data,
                     department_name=forms.department_name.data,
                     doctors_name=forms.doctors_name.data,
                     date= forms.date.data)
        db.session.add(user)
        db.session.commit()
        return render_template('index.html', forms=forms)
    return render_template('zapis.html', forms=forms)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'