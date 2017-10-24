class NumerosRomanos():
	def __init__(self):
		self.numero1="I"
		self.numero5="V"
		self.numero10="X"
		self.numero50="L"
		self.numero100="C"
		self.numero500="D"
		self.numero1000="M"

	def imprimirlista(self,listanueva):
		for i in listanueva:
			print(i, end="")


	def menorque5(self,numeroarabigo):
		self.elnumero=numeroarabigo
		self.i=1
		self.lista=[]
		if 0<self.elnumero<=3:			
			while self.i<=self.elnumero:
				self.lista.append(self.numero1)
				self.i=self.i+1
		elif self.elnumero==4:
			self.lista=["IV"]
		else:
			#lista=""
			pass
		return self.lista


	def menorque10(self, numeroarabigo):
		self.i=6
		self.lista=["V"]
		if 5<numeroarabigo<=8:
			while self.i<=numeroarabigo:
				self.lista.append(self.numero1)
				self.i=self.i+1
		elif numeroarabigo==9:
			self.lista=["IX"]
		else:
			self.lista=["V"]			
		return self.lista

	def menorque50(self, numeroarabigo):
		self.i=1
		self.lista=[]
		if 0<numeroarabigo<=3:
			while self.i<=numeroarabigo:
				self.lista.append(self.numero10)
				self.i=self.i+1
		elif numeroarabigo==4:
			self.lista=["XL"]
		else:
			#lista=""
			pass
		return self.lista

	def menorque100(self, numeroarabigo):
		self.i=6
		self.lista=["L"]
		if 5<numeroarabigo<=8:
			while self.i<=numeroarabigo:
				self.lista.append(self.numero10)
				self.i=self.i+1
		elif numeroarabigo==9:
			self.lista=["XC"]
		else:
			self.lista=["L"]
		return self.lista

	def menorque500(self, numeroarabigo):
		self.i=1
		self.lista=[]
		if 0<numeroarabigo<=3:
			while self.i<=numeroarabigo:
				self.lista.append(self.numero100)
				self.i=self.i+1
		elif numeroarabigo==4:
			self.lista=["CD"]
		else:
			#lista=""
			pass
		return self.lista

	def menorque1000(self, numeroarabigo):
		self.i=6
		self.lista=["D"]
		if 5<numeroarabigo<=8:
			while self.i<=numeroarabigo:
				self.lista.append(self.numero100)
				self.i=i+1
		elif numeroarabigo==9:
			self.lista=["CM"]
		else:
			self.lista=["D"]
		return self.lista

	def menorque5000(self, numeroarabigo):
		self.elnumero=numeroarabigo
		self.i=1
		self.lista=[]
		if 0<self.elnumero<=3:
			while self.i<=self.elnumero:
				self.lista.append(self.numero1000)
				self.i=self.i+1
		elif self.elnumero==4:
			self.lista=["MV"]
		else:
			#lista=""
			pass
		return self.lista



arabigo=input("Podrias introducir el numero a convertir: ")

minumero=NumerosRomanos()



for i in range(len(arabigo)):
	k=len(arabigo)-i
	if int(arabigo[i])<5 and k==1:
		minumero.imprimirlista(minumero.menorque5(int(arabigo[i])))				
	elif 5<=int(arabigo[i])<10 and k==1:
		minumero.imprimirlista(minumero.menorque10(int(arabigo[i])))	
	elif int(arabigo[i])<5 and k==2:
		minumero.imprimirlista(minumero.menorque50(int(arabigo[i])))	
	elif 5<=int(arabigo[i])<10 and k==2:
		minumero.imprimirlista(minumero.menorque100(int(arabigo[i])))	
	elif int(arabigo[i])<5 and k==3:
		minumero.imprimirlista(minumero.menorque500(int(arabigo[i])))	
	elif 5<=int(arabigo[i])<10 and k==3:
		minumero.imprimirlista(minumero.menorque1000(int(arabigo[i])))	
	elif int(arabigo[i])<5 and k==4:
		minumero.imprimirlista(minumero.menorque5000(int(arabigo[i])))	




 