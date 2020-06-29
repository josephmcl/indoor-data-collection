from flask import Blueprint, render_template, send_from_directory

FrontendAPI = Blueprint('frontend_api', __name__)

"""
@FrontendAPI.route('/')
def index():
    return '...', 200
"""

@FrontendAPI.route('/register/device')
def register_device():
    return render_template('register_device.html')

@FrontendAPI.route('/register/user')
def register_user():
    return render_template('register_user.html')


@FrontendAPI.route('/')
def dashboard():
    return render_template('dashboard.html')