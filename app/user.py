from flask import Blueprint, request, jsonify, current_app
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
        return jsonify({ 'message': 'Usuario Inserido com sucesso' }), 200

    return jsonify({ 'message': 'Email ja cadastrado' }), 401