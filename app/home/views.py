from flask import render_template, abort
from flask_login import login_required, current_user

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    :return: template home/index.html 
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required  # decorator, meaning that users must be logged in to access it.
def dashboard():
    """
    Render the dashoard template on the /dashboard route
    :return: template home/dashboard.html
    """
    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """
    Render the dashboard for admin
    :return: template home/admin_dashboard.html
    """
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html',
                           title="Dashboard")
