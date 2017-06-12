import numpy as np
import random

class GA(object):
	def __init__(self, populacao, limite, instancias, placa):
		self.geracao = []
		self.populacao = populacao
		self.limite = limite
		self.pecas = []
		self.instancias = instancias
		self.placa = placa
		pass

	def duplique(self):
		for i in self.instancias:
		    self.pecas.append(i)
		    if i[0] != i[1]:
		        peca = [i[1], i[0]]
		        self.pecas.append(peca)
		    pass
	def preprocessing(self):
		for i in range(0,len(self.pecas)):
			qtd = (self.placa[0] / self.pecas[i][0]) * (self.placa[1] / self.pecas[i][1])
			self.pecas[i].append(qtd)
			pass
		pass
		print self.pecas

	def generate(self):
		for i in range(0,self.populacao):
		    pop = random.sample(range(0, len(self.pecas)), len(self.pecas)) 
		    self.geracao.append(pop)
		return self.geracao
		pass

	def mutation(self):
		pass

	def crossover(self):
		pass

	def roleta(self):
		pass

	def evaluation(self):
		pass