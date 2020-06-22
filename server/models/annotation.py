from util.ext import db
from sqlalchemy.sql import func

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collection = db.Column(db.Text)
    data = db.Column(db.JSON)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def as_dict(self):
        return {
            'data':self.data,
            'created':self.created.strftime("%Y-%m-%d %H:%M:%S")}