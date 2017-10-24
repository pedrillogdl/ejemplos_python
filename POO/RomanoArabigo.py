class RomanoArabigo():
	def __init__(self):
		self.lista=["I", "V", "X", "L", "C", "D", "M"]
		self.sumatoria=0

	def validar(self, romano):
		self.numero=romano
		bandera=False
		contador=0
		for i in self.numero:
			if i.upper() in self.lista:
				contador=contador+1
			else:
				contador=0
				break
		if contador==0:
			bandera=False
			print("El Numero es invalido")
		else:
			bandera=True
		return bandera

	def enlistar(self, romano):
		self.lista=[]
		for i in romano:
			self.lista.append(i)
		return self.lista


	def analiza(self, nromano):
		self.milista=self.enlistar(nromano)
		i=0
		while i<(len(self.milista)-1) and i>=0:
			if i<len(self.milista):
				b=i
				if self.milista[i]=="I" and self.milista[i+1]=="V":
					self.sumatoria=self.sumatoria+4
					self.milista.remove(self.milista[i])
					self.milista.remove(self.milista[i])
					i=b					
				elif self.milista[i]=="I" and self.milista[i+1]=="X":
					self.sumatoria=self.sumatoria+9
					self.milista.remove(self.milista[i])
					self.milista.remove(self.milista[i])
					i=b
				elif self.milista[i]=="X" and self.milista[i+1]=="L":
					self.sumatoria=self.sumatoria+40
					self.milista.remove(self.milista[i])
					self.milista.remove(self.milista[i])
					i=b
				elif self.milista[i]=="X" and self.milista[i+1]=="C":
					self.sumatoria=self.sumatoria+90
					self.milista.remove(self.milista[i])
					self.milista.remove(self.milista[i])
					i=b
				elif self.milista[i]=="C" and self.milista[i+1]=="D":
					self.sumatoria=self.sumatoria+400
					self.milista.remove(self.milista[i])
					self.milista.remove(self.milista[i])
					i=b
				elif self.milista[i]=="C" and self.milista[i+1]=="M":
					self.sumatoria=self.sumatoria+900
					self.milista.remove(self.milista[i])
					self.milista.remove(self.milista[i])
					i=b
				elif self.milista[i]=="M" and self.milista[i+1]=="V":
					self.sumatoria=self.sumatoria+4000
					self.milista.remove(self.milista[i])
					self.milista.remove(self.milista[i])
					i=b
				else:
					i=i+1
		self.sumatoria=self.sumatoria+(self.lista.count("I")*1)
		self.sumatoria=self.sumatoria+(self.lista.count("V")*5)
		self.sumatoria=self.sumatoria+(self.lista.count("X")*10)
		self.sumatoria=self.sumatoria+(self.lista.count("L")*50)
		self.sumatoria=self.sumatoria+(self.lista.count("C")*100)
		self.sumatoria=self.sumatoria+(self.lista.count("D")*500)
		self.sumatoria=self.sumatoria+(self.lista.count("M")*1000)
		print("Tu numero Romano convertido al Arabigo es:")
		print(self.sumatoria)

Romano=RomanoArabigo()

validacion=False

while validacion!=True:
	minumero=input("Por favor introduce un numero romano: ")
	validacion=Romano.validar(minumero)

Romano.analiza(minumero)











