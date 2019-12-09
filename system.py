# Olexandr Stetsenko
# Last modified: 9/12/2019
# Description:
# Is a Small Bank system which consists to allow perform simple banking tasks
# like send money, view personal information and add or delete an accoutn of client
# The system is connected to a Postgresql database(local). There are two types of
# actors Administrator and Clients. Administrator add and delete clients. The clients
# manage their budgets by performin transactions. 

import psycopg2

class System:
  def __init__(self):
    self.hostnameD = '127.0.0.1'
    self.usernameD = 'postgres'
    self.passwordD = '' 
    self.database = 'SE1-Program'
    self.connection = psycopg2.connect("dbname ="+self.database+" user = "+self.usernameD+" password = "+self.passwordD+" host ="+self.hostnameD)
    self.cursor = self.connection.cursor()
    self.databaseCreated = False
    self.nextIdentification = 10000000

  def createClientDatabase(self):
    self.cursor.execute("DROP TABLE IF EXISTS Client;")
    create_table_query = """CREATE TABLE Client(
                            firstName VARCHAR,
                            lastName VARCHAR,
                            username VARCHAR,
                            password VARCHAR,
                            budget REAL,
                            identification INTEGER,
                            PRIMARY KEY(username,identification));"""
    self.cursor.execute(create_table_query)
    self.connection.commit()

  def addClient(self,firstName,lastName,username,password,identification):
    statement = "INSERT INTO Client VALUES('"+firstName+"','"+lastName+"','"+username+"','"+password+"',500,'"+identification+"')"
    self.cursor.execute(statement)
    self.connection.commit()

  def deleteClient(self,firstName,lastName,username):
    statement = "DELETE FROM Client WHERE Client.firstName = '"+firstName+"' and Client.lastName = '"+lastName+"' and Client.username = '"+username+"'"
    self.cursor.execute(statement)
    self.connection.commit()

  def existClient(self,username,password):
    statement = "SELECT * FROM Client WHERE username = '"+username+"' and password = '"+password+"'"
    self.cursor.execute(statement)
    found = self.cursor.fetchall()
    if len(found) > 0:
      return True
    else:
       return False

  def viewInfoClient(self,username,password):
    statement = "SELECT * FROM Client WHERE username = '"+username+"' and password = '"+password+"'"
    self.cursor.execute(statement)
    infoClient = self.cursor.fetchall()
    return infoClient

  def sendMoney(self,usernameSource,amount,identification):
    if amount <= 0:
      print("Invalid amount")
      return
    statement = "SELECT * FROM Client WHERE identification = "+identification
    self.cursor.execute(statement)
    infoDestClient = self.cursor.fetchall()
    if len(infoDestClient) > 0:
      infoDestClient = infoDestClient[0]
      statement = "SELECT * FROM Client WHERE username = '"+usernameSource+"'"
      self.cursor.execute(statement)
      infoSourceClient = self.cursor.fetchall()[0]
      if float(infoSourceClient[4]) < float(amount):
        print("Transaction is not possible, not enough money\n")
      else:

        statement = "UPDATE Client SET budget = "+str(float(infoSourceClient[4])-float(amount))+" WHERE client.username = '"+usernameSource+"'"
        self.cursor.execute(statement)
        statement = "UPDATE Client SET budget = "+str(float(infoSourceClient[4])+float(amount))+" WHERE client.identification = '"+identification+"'"
        self.cursor.execute(statement)
        self.connection.commit()
        print("Transaction success!\n")
    else:
      print("invalid identification!")



def main():
  print("Hello")
  system = System()
  system.createClientDatabase()
  system.databaseCreated = True
  while True: 
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if username == "system" and password =="system":
      cmd = input("Close Connection: ")
      if cmd.lower() == "yes":
        system.connection.close()
        print("Sysytem destroyed!")
        break

    elif username == "admin" and password == "admin":
      print("Welcome Administrator")
      while True:
        print("Your commands are as follow: addNewClient, deleteClient, logout")
        cmd = input("Please enter a command: ")
        
        if cmd == "addNewClient" and system.databaseCreated == True:
          print("Create new client:")
          firstNameC = input("Client first name: ")
          lastNameC = input("Client last name: ")
          usernameC = input("Client username: ")
          passwordC = input("Client password: ")
          system.addClient(firstNameC,lastNameC,usernameC,passwordC,str(system.nextIdentification))
          system.nextIdentification = system.nextIdentification + 1 
          print("Client is added to database!\n")

        elif cmd == "deleteClient" and system.databaseCreated == True:
          print("Create enter client information:")
          firstNameC = input("Client first name: ")
          lastNameC = input("Client last name: ")
          usernameC = input("Client username: ")
          system.deleteClient(firstNameC,lastNameC,usernameC)
          print("Client is deleted from database!\n")

        elif cmd == "logout":
          print("You are logout!\n")
          break

        else:
          print("Invalid Command!")

    elif system.existClient(username,password):
      infoClient = system.viewInfoClient(username,password)
      clientFirstName = infoClient[0][0]
      clientLastName = infoClient[0][1]
      print("Welcome",clientFirstName,clientLastName,"\n")
      while True:
        print("For doing a transaction, use command: sendMoney")
        print("If you want logout, use command: logout")
        print("For viewing the information of your account, use command: viewInfo\n")
        cmd = input("Please enter a command: ")
        if cmd == "sendMoney":
          amount = input("amount: ")
          identification = input("To identification: ")
          system.sendMoney(username,int(amount),identification)

        elif cmd == "viewInfo":
          infoClient = system.viewInfoClient(username,password)
          print("First Name:",infoClient[0][0])
          print("Last Name:",infoClient[0][1])
          print("Username:",infoClient[0][2])
          print("Password:",infoClient[0][3])
          print("Budget:",infoClient[0][4])
          print("Identification:",infoClient[0][5],"\n")

        elif cmd == "logout":
          print("You are logout!\n")
          break

        else:
          print("Invalid Command!")

    else:
      print("Invalid Username or password!\n")
main()
