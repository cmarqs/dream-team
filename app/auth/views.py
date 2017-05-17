from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    :return: redirect to auth.login route or stay in the page
    """
    form = RegistrationForm()

    # if not a post, load the registration template
    if not form.validate_on_submit():
        return render_template('auth/register.html',
                               form=form,
                               title='Register')

    # fill the form object
    employee = Employee(email = form.email.data,
                        username = form.username.data,
                        first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        password = form.password.data)

    # add employee to the database
    db.session.add(employee)
    db.session.commit()
    flash('You have sucessfully registered! You may now login.')

    # redirect to the login page
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    :return: redirect to home.dashboard if all's ok
    """
    form = LoginForm()

    # if not is a post, render the login template
    if form.validate_on_submit():
        # check whether employee exists in the database and
        # whether the password entered matches the password in the db
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            # log employee in
            login_user(employee)

            # redirect to the appropriate dashboard page
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
        else:  # stay in the page and warning the user
            flash('Invalid email or password.')

    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
