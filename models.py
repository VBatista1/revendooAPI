from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    senha = db.Column(db.String(10), unique=True, nullable=False)
    telefone = db.Column(db.String(12), unique=True, nullable=False)

    def __init__(self,name,email,senha,telefone):
        self.name=name
        self.email = email
        self.senha = senha
        self.telefone = telefone

    def __repr__(self):
        return '<User %r>' % self.name

class Produto(db.Model):
    __tablename__ = "tbProduto"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    marca = db.Column(db.String(20),  nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    venda = db.Column(db.Float, nullable=False)
    custo = db.Column(db.Float,  nullable=False)
    estoque = db.Column(db.Integer,  nullable=False)
    validade = db.Column(db.String(20), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, name, marca, descricao, venda, custo, estoque, validade,user_id):
        self.name = name
        self.marca = marca
        self.descricao = descricao
        self.venda = venda
        self.custo = custo
        self.estoque = estoque
        self.validade = validade
        self.user_id = user_id

    def __repr__(self):
        return '<Produto %r>' % self.name

class Clientes(db.Model):
    __tablename__ = "tbClientes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self,name,telefone,user_id):
        self.name = name
        self.telefone = telefone
        self.user_id = user_id

    def __repr__(self):
        return '<Cliente %r>' % self.name

class Vendas(db.Model):
    __tablename__ = "tbVendas"
    id = db.Column(db.Integer, primary_key=True)
    dataVenda = db.Column(db.String(20), nullable=True)
    dataEntrega = db.Column(db.String(20), nullable=True)
    pagamento = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.Integer,nullable=False)
    desconto = db.Column(db.Float,nullable=True)
    valorVenda = db.Column(db.Float,nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('tbProduto.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('tbClientes.id'))

    user = db.relationship('User', foreign_keys=user_id)
    produto = db.relationship('Produto', foreign_keys=produto_id)
    cliente = db.relationship('Clientes', foreign_keys=cliente_id)

    def __init__(self,dataVenda,dataEntrega,pagamento,quantidade,desconto,user_id,produto_id,cliente_id):
        self.user_id = user_id
        self.cliente_id = cliente_id
        self.produto_id = produto_id
        self.dataEntrega = dataEntrega
        self.dataVenda = dataVenda
        self.quantidade = quantidade
        self.desconto = desconto
        self.pagamento = pagamento

    def genValorVenda(self,valorProduto):
        valVenda = self.quantidade*valorProduto 
        self.valorVenda = valVenda - valVenda*self.desconto
        

    def __repr__(self):
        return '<Venda %r>' % self.id

