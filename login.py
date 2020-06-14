
from datetime import timedelta
from flask import Blueprint, request, jsonify, current_app, make_response
#from flask_jwt_extended import create_access_token, create_refresh_token
from models import User
from serealizer import UserSchema,user_schema

bp_login = Blueprint('login', __name__)
@bp_login.route('/login', methods=['POST'])
def login():
    #user, error = UserSchema().load(request.json)
    #print(user)

    email = request.json['email']
    senha = request.json['senha']

    print(email,senha)

    try:
        user = User.query.filter(User.email == str(email), User.senha == str(senha)).first()

        if user!=None:
            result = user_schema.dump(user)
            resp = make_response("OK")
            resp.status_code = 201
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = '*'
            resp.headers['Access-Control-Allow-Domain'] = '*'
            resp.headers['Access-Control-Allow-Credentials'] = True
            return resp
        resp = make_response("Not Ok")
        resp.status_code = 403
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        resp.headers['Access-Control-Allow-Domain'] = '*'
        resp.headers['Access-Control-Allow-Credentials'] = True
        return resp
    except Exception as e:
        print(str(e))
        return jsonify(str(e)), 400

