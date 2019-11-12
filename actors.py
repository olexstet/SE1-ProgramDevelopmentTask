# Stetsenko Olexandtr 
# Actors 
# Description:
# In this file, we have the structure(classes) how actors 
# are defined. 
class actAdmin():
	def __init__(self,fisrtName,lastName,username,password):
		self.fisrtName = fisrtName
		self.lastName = lastName
		self.username = username 
		self.password = password


class actClient():
	def __init__(self,fisrtName,lastName,username,password, initialAmount):
		self.fisrtName = fisrtName
		self.lastName = lastName
		self.username = username 
		self.password = password
		self.amount = initialAmount
