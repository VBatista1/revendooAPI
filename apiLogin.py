from flask import Flask, request, jsonify
from flask_cors import CORS
from dbUsuario import dbUser
import time
p = dbUser('sql210.main-hosting.eu','u835930476_revendoo','123456','u835930476_revendoo')
#import requests
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return 'Seja bem vindo ao revendooAPI'

@app.route("/login", methods=["POST"])
def login():
    if request.method == 'POST':
        dados = request.get_json()
        print('dados', dados)
        login = dados.get('email')
        senha = dados.get('senha')
        if senha != None and login !=None:
            try:
                res = p.loginUsuario(login,senha)
                usuario = res[0]
                if res != []:
                    return jsonify(
                    {
                        'id':str(usuario[0]),
                    }
                    )
                else:
                    return jsonify({'id':'Login Invalido'})
            except Exception as e:
                return jsonify({'id':'Login Invalido'})
        else:
            return jsonify({'erro':'Parametros invalidos'})
    else:
        return jsonify({'aguardando':'Parametros'})

@app.route("/cadastroUsuario", methods=["POST"])
def cadastroUsuario():
    dados = request.get_json(force=True)
    nome = dados['nome']
    telefone = dados['telefone']
    email = dados['email']
    cpf = dados['cpf']
    senha = dados['senha']
    print(dados)
    print(nome,telefone,email,cpf,senha)
    try:
        findEmail = p.findUsuario_by_CPF(cpf)
        if len(findEmail) == 0:
            p.insertUsuario(nome,telefone,email,senha,cpf)
            time.sleep(5)
            res = p.findUsuario_by_CPF(cpf)
            iD = res[0]
            return jsonify({'mensagem':'Cadastro feito com sucesso','id':str(iD[0])})
        else:
            return jsonify({'mensagem':'Email ja em uso'})
    except Exception as e:
        print(e)
        return jsonify({'erro':e})

if __name__ == '__main__':
  app.run(debug=True)