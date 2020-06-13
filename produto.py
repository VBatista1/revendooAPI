from flask import Blueprint, request, jsonify, current_app
from models import Produto
from serealizer import ProdutoSchema,produto_schema
bp_produto = Blueprint('produto', __name__)


@bp_produto.route('/create-produto/<idUser>', methods=['POST'])
def createProduto(idUser):
    name = request.json['name']
    marca =  request.json['marca']
    descricao =  request.json['descricao']
    venda = request.json['venda']
    custo = request.json['custo']
    estoque = request.json['estoque']
    validade = request.json['validade']
    
    produto = Produto.query.filter(Produto.name == str(name)).first()

    if produto == None:
        p = Produto(name=name,marca=marca,descricao=descricao,venda=float(venda),custo=float(custo),estoque=int(estoque),validade=validade,user_id=idUser)
        current_app.db.session.add(p)
        current_app.db.session.commit()
        return jsonify({ 'message': 'Produto Inserido com sucesso' }

    return jsonify({ 'message': 'Produto ja cadastrado' })

@bp_produto.route('/produtos', methods=['GET'])
def readProdutos():
    result = Produto.query.all()
    return jsonify(produto_schema.dumps(result))

@bp_produto.route('/produtos/<idUser>', methods=['GET'])
def readProdutos_by_userID(idUser):
    result = Produto.query.filter(Produto.user_id == idUser)
    return jsonify(produto_schema.dumps(result))

@bp_produto.route('/produto', methods=['GET'])
def readProdutos_by_userID_id():
    idUser = request.args.get('idUser')
    produtoID = request.args.get('idProduto')
    result = Produto.query.filter(Produto.user_id == idUser, Produto.id == int(produtoID))
    return jsonify(produto_schema.dumps(result))