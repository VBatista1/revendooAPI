from flask import Blueprint, request, jsonify, current_app
from .models import Clientes
from .serealizer import cliente_schema
bp_cliente = Blueprint('cliente', __name__)


@bp_cliente.route('/create-cliente/<idUser>', methods=['POST'])
def createCliente(idUser):
    name = request.json['name']
    telefone =  request.json['telefone']
    
    cliente = Clientes.query.filter(Clientes.telefone == str(telefone),Clientes.user_id==idUser).first()
    if cliente == None:
        c = Clientes(name=name,user_id=idUser,telefone=telefone)
        current_app.db.session.add(c)
        current_app.db.session.commit()
        return jsonify({ 'message': 'Cliente Inserido com sucesso' }), 200

    return jsonify({ 'message': 'Cliente já cadastrado' }), 401

@bp_cliente.route('/clientes/<idUser>', methods=['GET'])
def selectCliente_byUser(idUser):
    result = Clientes.query.filter(Clientes.user_id==idUser)
    return cliente_schema.dumps(result), 200


@bp_cliente.route('/cliente', methods=['GET'])
def readClientes_by_userID_id():
    idUser = request.args.get('idUser')
    clienteID = request.args.get('idCliente')
    result = Clientes.query.filter(Clientes.user_id == idUser, Clientes.id == int(clienteID))
    return cliente_schema.dumps(result), 200