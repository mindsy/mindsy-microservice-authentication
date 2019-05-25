import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.login import UserLogin, UserLogout

from blacklist import BLACKLIST

app = Flask(__name__)
load_dotenv(".env")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = os.environ.get("APP_SECRET_KEY")
app.config['JWT_SECRET_KEY'] = 'mindsy-microservice-register'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
api = Api(app)

jwt = JWTManager(app)


# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST  # Here we blacklist particular JWTs that have been created in the past.


# The following callbacks are used for customizing jwt response/error messages.
# The original ones may not be in a very pretty format (opinionated)
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        "description": "The token is not fresh.",
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        "description": "The token has been revoked.",
        'error': 'token_revoked'
    }), 401


api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout/<string:crp>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')