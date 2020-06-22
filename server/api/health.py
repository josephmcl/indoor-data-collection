from flask import Blueprint

HealthAPI = Blueprint('health_api', __name__)

@HealthAPI.route('/')
def index():
    return '...', 200