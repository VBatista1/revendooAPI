from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from models import User,Produto
from marshmallow_sqlalchemy import ModelSchema
ma = Marshmallow()


def configure(app):
    ma.init_app(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","email", "name")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class ProdutoSchema(ma.Schema):
    class Meta:
        fields = ("id","name","descricao","venda","custo","estoque","validade")

produto_schema = ProdutoSchema()
produto_schema = ProdutoSchema(many=True)

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ("id","name","telefone","user_id")

cliente_schema = ClienteSchema()
cliente_schema = ClienteSchema(many=True)
