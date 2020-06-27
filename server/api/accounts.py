from flask import Blueprint, request, jsonify
from util.ext import guard, db
from models.user import User

AccountsAPI = Blueprint('accounts_api', __name__)

def get_creds(request):
    username = request.get_json('username')
    password = request.get_json('password')
    if username is None or password is None:
        return None
    username = username.get('username')
    password = password.get('password')
    return (username, password)

@AccountsAPI.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(db.session.query(User.username).all()), 200

    elif request.method == 'POST':
        creds = get_creds(request)
        if creds is None:
            return jsonify({'status':'Expected username and password.'}), 400
        username, password = creds
        user = User(username=username, password=guard.hash_password(password))
        if not user.create(username):
            return jsonify({'status':'Username already exists.'}), 409
        else:
            return jsonify({'status':'User created.'}), 201

@AccountsAPI.route('/login/', methods=['POST'])
def login():
    creds = get_creds(request)
    if creds is None:
        return jsonify({'status':'Expected username and password.'}), 400
    username, password = creds
    if not User.exists(username):
        return jsonify({'status':'Login information incorrect.'}), 409
    user = guard.authenticate(username, password)
    return jsonify({'access_token': guard.encode_jwt_token(user)}), 200

@AccountsAPI.route('/logout/', methods=['POST'])
def logout():
    return '', 200

"""
@AccountsAPI.route('/protected', methods=['GET'])
@guard.auth_required
def protected():
    return jsonify(message='protected endpoint (allowed user {})'.format(
        flask_praetorian.current_user().username,
    ))
"""