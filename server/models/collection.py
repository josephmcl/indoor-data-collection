from util.ext import db
from sqlalchemy.sql import func

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    title = db.Column(db.Text)
    creator = db.Column(db.Text)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    @classmethod
    def exists(cls, name):
        return db.session.query(db.exists().where( \
            Collection.name == name)).scalar()
