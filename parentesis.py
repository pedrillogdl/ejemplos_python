class Parentesis():
	def __init__(self):
		self.curvos1=('(')
		self.curvos2=(')')
		self.cuadrados1=('[')
		self.cuadrados2=(']')
		self.llaves1=('{')
		self.llaves2=('}')


	def verificar(self, parentesisr):
		self.parentesisl=[""]
		for i in parentesisr:
			self.parentesisl.append(i)


		self.curv1=self.parentesisl.count(self.curvos1)
		self.curv2=self.parentesisl.count(self.curvos2)
		self.cuad1=self.parentesisl.count(self.cuadrados1)
		self.cuad2=self.parentesisl.count(self.cuadrados2)
		self.llave1=self.parentesisl.count(self.llaves1)
		self.llave2=self.parentesisl.count(self.llaves2)


		self.b=True

		for i in range(len(parentesisr)):
			if parentesisr[i]  in self.curvos2 and i==0:
				self.b=False
			elif parentesisr[i] in self.curvos2 and i>0:
				c=i-1
				while c>=0:
					if parentesisr[c] in self.curvos1:
						self.b=True
						break
					else:
						self.b=False
					c=c-1
			elif parentesisr[i]  in self.cuadrados2 and i==0:
				self.b=False
			elif parentesisr[i] in self.cuadrados2 and i>0:
				c=i-1
				while c>=0:
					if parentesisr[c] in self.cuadrados1:
						self.b=True
						break
					else:
						self.b=False
					c=c-1
			elif parentesisr[i]  in self.llaves2 and i==0:
				self.b=False
			elif parentesisr[i] in self.llaves2 and i>0:
				c=i-1
				while c>=0:
					if parentesisr[c] in self.llaves1:
						self.b=True
						break
					else:
						self.b=False
					c=c-1



		if self.curv1==self.curv2 and self.cuad1==self.cuad2 and self.llave1==self.llave2 and self.b==True:
			print("La estructura de parentesis es valida")
		else:
			print("La estructura de parentesis es invalida")


estructura=input("Por favor introduce una estructura de parentesis: ")

MisParentesis=Parentesis()

MisParentesis.verificar(estructura)




#naditanada
		





