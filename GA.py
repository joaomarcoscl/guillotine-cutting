import numpy as np
import random

class GA(object):
	def __init__(self, populacao, instancias, placa, mutation, crossover):
		self.geracao = []
		self.populacao = populacao
		self.pecas = []
		self.instancias = instancias
		self.placa = placa
		self.mutation = mutation
		self.crossover = crossover
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
		return np.matrix(self.pecas)

	def generate(self):
		for i in range(0,self.populacao):
		    pop = random.sample(range(0, len(self.pecas)), len(self.pecas)) 
		    self.geracao.append(pop)
		pass
		return np.matrix(self.geracao)

	def mutation(self):
		pass

	def crossover(self):
		pass

	def roulette(self):
		pass

	def evaluation(self):
		pass