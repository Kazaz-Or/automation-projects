import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, JWTError

from FlaskAPITesting.auth import authenticate, identity
from FlaskAPITesting.resources.item import Item, ItemList
from FlaskAPITesting.resources.store import Store, StoreList
from FlaskAPITesting.resources.user import UserRegister

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "strongpass123"

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


@app.errorhandler(JWTError)
def auth_error_handler(err):
    return {'message': 'Could not authorize, check your authorization header.'}, 401


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
