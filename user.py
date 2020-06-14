from flask import Blueprint, request, jsonify, current_app, make_response
from serealizer import UserSchema
from models import User

bp_user = Blueprint('user', __name__)


@bp_user.route('/create-user', methods=['POST'])

def register():
    email = request.json['email']
    senha = request.json['senha']
    telefone = request.json['telefone']
    name = request.json['name']
    print(email,senha,telefone,name)
    user = User.query.filter(User.email == str(email)).first()
    if user == None:
        u = User(name,email,senha, telefone)
        current_app.db.session.add(u)
        current_app.db.session.commit()
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