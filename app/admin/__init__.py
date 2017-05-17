from flask import Blueprint

"""
 In each blueprint's __init__.py file, we need to create a Blueprint object and
 initialize it with a name. We also need to import the views.
"""
admin = Blueprint("admin", __name__)
from . import views
