# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_raw_jwt
)
from security import check_encrypted_password
from static.imports import *

from blacklist import BLACKLIST


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('crp',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    @classmethod
    def post(cls):
        data = UserLogin.parser.parse_args()
        psychologist = PsychologistModel.find_by_crp(data['crp'])
        decrypted_password = check_encrypted_password(data['password'], psychologist.password)

        if psychologist and decrypted_password:
            access_token = create_access_token(identity=psychologist.PERSON.id, fresh=True)
            psychologist.token = access_token
            psychologist.save_to_db()
            return {'access_token': access_token}, 200

        return {'message': 'Invalid Credentials'}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self, crp):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        psychologist = PsychologistModel.find_by_crp(crp)
        psychologist.token = None
        psychologist.save_to_db()
        return {'message': 'Successfully logged out'}, 200
