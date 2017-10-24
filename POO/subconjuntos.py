class Subconjuntos():

	def seccionar(self, conjunto):
		self.lista=[]
		self.contador=0
		for i in conjunto:
			self.lista.append(i)
			self.contador=self.contador+1
		b=0
		self.newmember=""
		self.newlista=[]
		while b<self.contador:
			c=b
			while c<(self.contador):
				self.newmember=self.newmember+self.lista[c]
				self.newlista.append(self.newmember)
				c=c+1


