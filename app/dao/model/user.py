from marshmallow import Schema, fields
from app.setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(100))


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    password = fields.Str()
    role = fields.Str()