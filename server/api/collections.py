from flask import Blueprint, request, jsonify
from util.token import make_token
from util.ext import db
from models.collection import Collection
from models.annotation import Annotation
import flask_praetorian
import jsonschema
import json

CollectionsAPI = Blueprint('collections_api', __name__)

def annotations_for(name):
    query = db.session.query(Annotation).filter(Annotation.collection == name).all()
    return json.dumps([row.as_dict() for row in query])

schema = {
    'type':'object',
    'properties':{
        'x':{'type':'number'},
        'y':{'type':'number'},
        'z':{'type':'number'},
        'lx':{'type':'number'}
    },
    'required': ['x', 'y']
}

def validate(datum):
    try:
        jsonschema.validate(datum, schema)
    except jsonschema.exceptions.ValidationError as e:
        return False
    except json.decoder.JSONDecodeError as e:
        return False
    return True

def validate_and_commit_json(name, data):
    if isinstance(data, (list)):
        for d in data:
            if not validate(d):
                return False
        for d in data:
            annotation = Annotation(collection=name, data=d)
            db.session.add(annotation)
        db.session.commit()
        return True
    elif isinstance(data, (dict)):
        if not validate(data):
            return False
        annotation = Annotation(collection=name, data=data)
        db.session.add(annotation)
        db.session.commit()
        return True
    else:
        return False


@CollectionsAPI.route('/', methods=['GET', 'POST'])
@flask_praetorian.auth_required
def index():
    if request.method == 'GET':
        return jsonify(db.session.query(Collection.name).all()), 200
    elif request.method == 'POST':
        name = make_token()
        collection = Collection(name=name, title=name, \
            creator=flask_praetorian.current_user().username)
        db.session.add(collection)
        db.session.commit()
        return jsonify({'location':f'/collections/{name}/'}), 201

@CollectionsAPI.route('/<string:name>/', methods=['GET', 'PUT'])
@flask_praetorian.auth_required
def collection(name):
    if not Collection.exists(name):
        return jsonify({'status':'Resource does not exist.'}), 405
    if request.method == 'GET':
        return annotations_for(name), 200
    elif request.method == 'PUT':
        if not request.is_json:
            return jsonify({'status':'Expected JSON.'}), 400
        data = request.get_json()
        annotation = Annotation(collection=name, data=data)
        if not validate_and_commit_json(name, data):
            return jsonify({'status':'Poorly formatted JSON.'}), 400
        return jsonify({'status':'Annotation data added.'}), 202
