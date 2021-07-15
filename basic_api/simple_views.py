import flask
from flask_restful import Api, Resource


class SimpleApiResource(Resource):
    def get(self):
        return {"hello": ":)"}


mod = flask.Blueprint("api", __name__, url_prefix="/api")
api = Api(mod)
api.add_resource(SimpleApiResource, "/me")
