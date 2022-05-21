from flask import flash, redirect, render_template, request, url_for
from ..email import mail_message
from .forms import LoginForm, RegistrationForm
from . import auth
from ..models import User 
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message
from werkzeug.security import generate_password_hash,check_password_hash




@auth.route('/register',methods =['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
      
        db.session(user)
        db.session.commit()

        mail_message("Welcome to the BLOG","email/welcome",user.email,user=user)

        return redirect(url_for('auth.login'))
        
        
    title = "Account registered"
    return render_template('auth/register.html',form = form)


@auth.route('/login',methods =['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash("Invalid credentials")

    title = 'Login'
    return render_template('auth/login.html',form=form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

    



