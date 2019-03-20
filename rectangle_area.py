class rectangulo:
	def cargar(self,L,A):
		self.largo=L
		self.ancho=A
	def calcular(self):
		p=(2*self.largo)+(2*self.ancho)
		a=self.largo*self.ancho
		self.perimetro=p
		self.area=a
	def imprimir(self):
		print "Largo es: ",self.largo
		print "Ancho es: ",self.ancho
		print "Perimetro es: ",self.perimetro
		print "Area es: ",self.area