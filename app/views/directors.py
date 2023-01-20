from flask import request
from flask_restx import Resource, Namespace
from app.dao.model.director import DirectorSchema
from app.implemented import director_service
from app.helpers.decorators import auth_required, admin_required

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        data = request.json
        director = director_service.create(data)
        return "", 201, {"location": f"/directors/{director.id}"}

@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, did):
        data = request.json
        director_service.update(did, data)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204