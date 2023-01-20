from flask import request
from flask_restx import Resource, Namespace
from app.dao.model.genre import GenreSchema
from app.implemented import genre_service
from app.helpers.decorators import auth_required, admin_required

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenreView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        data = request.json
        genre = genre_service.create(data)
        return "", 201, {"location": f"/genres/{genre.id}"}


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid):
        data = request.json
        genre_service.update(gid, data)
        return "", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204