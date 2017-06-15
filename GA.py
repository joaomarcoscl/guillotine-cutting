import numpy as np
import random

class GA(object):
	def __init__(self, populacao, instancias, placa, mutation, crossover):
		self.geracao = []
		self.populacao = populacao
		self.pecas = []
		self.pesos = []
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
		    peso = []
		    for x in pop:
		    	peso.append(random.sample(range(0, self.pecas[x][2]+1), 1)[0])
		    	pass
		    self.pesos.append(peso)
		    self.geracao.append(pop)
		pass

	def mutation(self):
		pass

	def crossover(self):
		pass

	def roulette(self):
		pass

	def evaluation(self):
		menor = 1
		menorsolucao = 0
		for i in range(0,self.populacao):
			solucao = dict()
			area = 0
			indice = 0
			maioraltura = 0
			altura = self.placa[1]
			largura = self.placa[0]
			
			for x in range(0, len(self.geracao[i])):
				quantidadepeca = self.pesos[i][x]
				alturapeca = self.pecas[self.geracao[i][x]][1]
				largurapeca = self.pecas[self.geracao[i][x]][0]
				for z in range(0, quantidadepeca):

					if area + largurapeca > largura:
						area = 0
						indice+=1
						altura = altura - maioraltura
						maioraltura = 0	

					if area + largurapeca <= largura and altura >= 0 and alturapeca < altura:
						area+=largurapeca
						if indice in solucao:
							solucao[indice].append(self.pecas[self.geracao[i][x]])
						else:
							solucao[indice] = [self.pecas[self.geracao[i][x]]]
						if self.pecas[self.geracao[i][x]][1] > maioraltura:
							maioraltura = self.pecas[self.geracao[i][x]][1]
				
			areasolucao = 0
			for s in solucao.values():
				for k in s:
					areasolucao += k[0]*k[1]
	
			perca = float((self.placa[1]*self.placa[0]) - areasolucao) / float(self.placa[1]*self.placa[0])
			if perca  < menor:
				menor = perca
				menorsolucao = solucao

		print menor
		print menorsolucao
		pass