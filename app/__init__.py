from flask import Flask
from flask_migrate import Migrate
#from flask_jwt_extended import JWTManager
from models import configure as config_db
from serealizer import configure as config_ma
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://b13febca5980fe:9c4ead86@us-cdbr-east-06.cleardb.net/heroku_a23d77c529f2361"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
CORS(app)
config_db(app)
config_ma(app)

Migrate(app, app.db)

from login import bp_login
app.register_blueprint(bp_login)

from user import bp_user
app.register_blueprint(bp_user)

from produto import bp_produto
app.register_blueprint(bp_produto)

from cliente import bp_cliente
app.register_blueprint(bp_cliente)

from vendas import bp_venda
app.register_blueprint(bp_venda)
    
if __name__ == '__main__':
  app.run(debug=True)