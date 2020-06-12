
from datetime import timedelta
from flask import Blueprint, request, jsonify, current_app
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
            return jsonify(result)

        return jsonify({
                'message': 'Credenciais invalidas'
        }), 401
    except Exception as e:
        print(str(e))
        return jsonify(str(e)), 400

