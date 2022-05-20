from flask import flash, redirect, render_template, request, url_for
from ..email import mail_message
from .forms import LoginForm, RegistrationForm
from . import auth
from ..models import User 
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message




@auth.route('/register')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        con_password = form.con_password.data
        new_register = User(username,email,password,con_password)
        db.session(new_register)
        db.session.commit()

        mail_message("Welcome to the BLOG","email/welcome",new_register.email,user=new_register)

        return redirect(url_for('auth.login'))
        
        
    title = "Account registered"
    return render_template('auth/register.html',form = form,title=title)


@auth.route('/login')
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

    



