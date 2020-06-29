from flask import Flask
from api.health import HealthAPI 
from api.collections import CollectionsAPI 
from api.accounts import AccountsAPI 
from api.frontend import FrontendAPI
from models.user import User
from util.ext import db, guard
import random
import time

def register_blueprints(app):
    app.register_blueprint(HealthAPI, url_prefix='/health')
    app.register_blueprint(CollectionsAPI, url_prefix='/collections')
    app.register_blueprint(AccountsAPI, url_prefix='/accounts')
    app.register_blueprint(FrontendAPI, url_prefix='/')

def init_extentsions(app):
    db.init_app(app)
    guard.init_app(app, User)

def init_app():
    random.seed(time.time())

    app = Flask(__name__)
    app.config.from_object('settings')

    init_extentsions(app)
    register_blueprints(app)
    
    with app.app_context():
        db.create_all()
    return app

app = init_app()

if __name__ == '__main__':


    app.run(host='0.0.0.0', port=5000, debug=True) 