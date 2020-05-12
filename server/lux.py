from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Don\'t talk to me'

@app.route('/api/add_message/', methods=['POST'])
def add_message(uuid):
    content = request.json
    print(content)
    data = {'message': 'Created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)


