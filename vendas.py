from flask import Blueprint, request, jsonify, current_app, make_response
from models import Produto
from models import Produto,Clientes,User,Vendas
from serealizer import ProdutoSchema,produto_schema
bp_venda = Blueprint('venda', __name__)

@bp_venda.route('/venda', methods=['POST'])
def fazerVenda():
    idUser = int(request.json['idUser'])
    clienteID = int(request.json['clienteID'])
    produtoID = int(request.json['produtoID'])

    datavenda = request.json['dataVenda']
    dataentrega = request.json['dataEntrega']
    pagamento = request.json['pagamento']
    quantidade = int(request.json['quantidade'])
    desconto = float(request.json['desconto'])

    produto = Produto.query.filter(Produto.id == produtoID, Produto.user_id == idUser).first()

    estoque = produto.estoque

    dif = estoque-quantidade

    if dif >= 0:
        v = Vendas(dataVenda=datavenda,dataEntrega=dataentrega,pagamento=pagamento,quantidade=quantidade,desconto=desconto,user_id=idUser,cliente_id=clienteID,produto_id=produtoID)
        v.genValorVenda(valorProduto=float(produto.venda))
        current_app.db.session.add(v)
        
        produto.estoque = dif
    
        current_app.db.session.commit()

        resp = make_response("OK")
        resp.status_code = 201
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        resp.headers['Access-Control-Allow-Domain'] = '*'
        resp.headers['Access-Control-Allow-Credentials'] = True
        return resp

    else:
        resp = make_response("Not Ok")
        resp.status_code = 403
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        resp.headers['Access-Control-Allow-Domain'] = '*'
        resp.headers['Access-Control-Allow-Credentials'] = True
        return resp