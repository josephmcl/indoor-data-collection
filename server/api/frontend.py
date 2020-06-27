from flask import Blueprint, render_template

FrontendAPI = Blueprint('frontend_api', __name__)

@FrontendAPI.route('/')
def index():
    return '...', 200

@FrontendAPI.route('/register')
def register():
    return render_template('register.html')