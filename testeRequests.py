import requests

def testelogin():
    login = {
        "login":"vitor@gmail.com", 
        "senha":"senha"
    }
    r = requests.post(url="http://127.0.0.1:5000/login",data=login)
    print(r.text)
def testeCadastro():
    login = {
        "nome":"vitor@gmail.com", 
        "cpf":"2398756",
        "telefone":"29256960",
        "email":"teste@tes.com",
        "senha":"pass"
    }
    r = requests.post(url="http://127.0.0.1:5000/cadastroUsuario",data=login)
    print(r.text)

testeCadastro()