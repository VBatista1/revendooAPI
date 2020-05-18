import mysql.connector
import time
class dbUser:
  def __init__(self,host,user,passwd,database):
      self.mydb = mysql.connector.connect(
      host=host,
      user=user,
      passwd=passwd,
      database=database,
      connect_timeout=1000
      )
      self.mycursor = self.mydb.cursor()

  def getUsuarios(self):
    sql = "SELECT * FROM usuario"
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    listaUsuarios = []
    for x in myresult:
      listaUsuarios.append(x)
      #print(x[1])
    return listaUsuarios

  def insertUsuario(self,nome,telefone,email,senha,cpf):
    sql = "insert into usuario(nome,telefone,email,senha,cpf) values(%s,%s,%s,%s,%s);"
    val = (nome,telefone,email,senha,cpf)
    self.mycursor.execute(sql,val)
    self.mydb.commit()
    print(self.mycursor.rowcount, "record inserted.")

  def findUsuario_by_ID(self,iD):
    sql = "SELECT * FROM usuario WHERE id=%s;"%iD
    #print(sql)
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    print(myresult)
    return myresult

  def findUsuario_by_EMAIL(self,iD):
    email = str(iD)
    print(email)
    sql = "SELECT * FROM usuario WHERE email='%s';"%email
    print(sql)
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    print(myresult)
    return myresult

  def findUsuario_by_CPF(self,iD):
    sql = "SELECT * FROM usuario WHERE cpf='%s';"%iD
    #print(sql)
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    print(myresult)
    return myresult

  def delete_by_ID(self,iD):
    sql = "DELETE FROM usuario WHERE id=%s;"%iD
    self.mycursor.execute(sql)
    self.mydb.commit()
    print(self.mycursor.rowcount, "record(s) deleted")

  def updateUsuario(self,iD,nome,telefone,email,senha):
    sql = "UPDATE customers SET nome = %s, telefone=%s, email=%s, senha=%s WHERE id ="+str(iD)
    self.mycursor.execute(sql)
    self.mydb.commit()
    print(self.mycursor.rowcount, "record(s) affected")

  def loginUsuario(self,email,senha):
    print(email, senha)
    sql = "SELECT * FROM usuario WHERE email='"+str(email)+"' and senha='"+str(senha)+"';"
    val = (email,senha)
    print(sql)
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    print(myresult)
    return myresult
