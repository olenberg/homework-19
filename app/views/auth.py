from flask import request, abort
from flask_restx import Resource, Namespace
from app.implemented import auth_service

auth_ns = Namespace("auth")

@auth_ns.route('/')
class AuthViews(Resource):
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if None in [username, password]:
            abort(400)

        tokens = auth_service.generate_tokens(username, password)

        if not tokens:
            return abort(401)

        return tokens, 201

    def put(self):
        data = request.json
        token = data.get("refresh_token")
        tokens = auth_service.approve_refresh_token(token)

        if not tokens:
            return abort(401)

        return tokens, 201
