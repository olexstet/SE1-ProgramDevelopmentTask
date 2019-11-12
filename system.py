
# Stetsenko Olexandr 
# System code source
# Description:
# This file contains python's codes for the system. 
# Here system is initialized and created 
# In system we have different operations that can be call by the actors 
import psycopg2
from actors import * 

hostname = '127.0.0.1'
username = 'postgres'
password = ''
database = 'SE1-Program'

class system:
  def __init__(self,name):
    self.name = name
    self.user = None
    
  def createAdmin(fisrtName,lastName,username,password):
    cursor = databaseConnection(actor,database,username,password,localhost)
    statement = "INSERT INTO Admin VALUES("+str(fisrtName)+","+str(lastName)+","+str(username)+","+str(password)+")"
    cursor.execute(statement)

  def createClient(fisrtName,lastName,username,password, initialAmount):
    cursor = databaseConnection(actor,database,username,password,localhost)
    statement = "INSERT INTO Admin VALUES("+str(fisrtName)+","+str(lastName)+","+str(username)+","+str(password)+","+float(initialAmount)+")"
    cursor.execute(statement)

  def createClientInstance(username,password,fisrtName,lastName):
    client = actClient(fisrtName,lastName,username,password,500)
    return client 

  def createAdminInstance(username,password,fisrtName,lastName):
    client = actAdmin(fisrtName,lastName,username,password)
    return client

  def login(username,password):
    cursor = databaseConnection(actor,database,username,password,localhost)
    cursor.execute("SELECT username,password,fisrtName,lastName FROM Client")
    listClient = cursor.fetchall()
    for user in listClient:
      if user[0] == "username" and user[1] == "password":
        self.user = createClientInstance(username,password,fisrtName,lastName)
        print("You are succesfully logged. Welcome!")
        return

    cursor.execute("SELECT username,password,fisrtName,lastName FROM Admin")
    listAdmin = cursor.fetchall()
    for user in listAdmin:
      if user[0] == "username" and user[1] == "password":
        self.user = createAdminInstance(username,password,fisrtName,lastName)
        print("You are succesfully logged. Welcome!")
        return

  def logout():
    self.user = None
    print("Succesfully exit the system. See you next time!")
    return 

  def oeSentMoney(firstName, lastName,amount):
    cursor = databaseConnection(actor,database,username,password,localhost)
    usernameSender = self.user.username
    cursor.execute("SELECT username,amount FROM Client WHERE firstName ="+str(firstName)+", lastName ="+str(lastName))
    result = cursor.fetchall()
    usernameReceiver,amountReceiver = result[0], result[1]
    amountReceiver += amount
    statement = "SELECT amount"
    cursor.execute()
             	
  def databaseConnection(actor,database,username,password,localhost):
    connection = psycopg2.connect("dbname ="+database+" user = "+username+" password = "+password+" host = "+localhost)
    cursor = connection.cursor()
    return cursor

  def createDatabase(actor,database,username,password,localhost):
    cursor = databaseConnection(actor,database,username,password,localhost)
    if(type(actor).__name__ == "actClient"):
      cursor.execute("DROP TABLE IF EXISTS Client;")

      create_table_query = '''CREATE TABLE Client(
          					FirstName VARCHAR(255),
          					LastName VARCHAR(255),
          					Username VARCHAR(255),
          					Password VARCHAR(255),
          					Amount REAL,
          					PRIMARY KEY(Username)
                                              );'''
      cursor.execute(create_table_query)

    if type(actor).__name__ == "actAdmin":
      cursor.execute("DROP TABLE IF EXISTS Admin;")
      create_table_query = '''CREATE TABLE Admin(
          					FirstName VARCHAR(255),
          					LastName VARCHAR(255),
          					Username VARCHAR(255),
          					Password VARCHAR(255),
          					PRIMARY KEY(Username)
                                                      );'''
      cursor.execute(create_table_query)
                 



def main():
  admin = createAdmin("Olexandr","Stetsenko","olex","stet")
  
  

		











