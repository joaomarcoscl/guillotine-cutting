import numpy as np
import random
import operator

class GA(object):
	
	def __init__(self, populacao, instancias, placa, mutation, crossover):
		self.geracao = []
		self.populacao = populacao
		self.pecas = []
		self.pesos = []
		self.instancias = instancias
		self.placa = placa
		self.ratemutation = mutation
		self.ratecrossover = crossover
		self.percas = []
		self.solucao = {'menor': 1}
		self.execucao = 0

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
		    pop.append(0)
		    self.pesos.append(peso)
		    self.geracao.append(pop)
		pass

	def mutation(self):
		mutations =  random.sample(range(0, self.populacao), int(self.ratemutation * self.populacao))
		for i in range(0, len(mutations), 2):
			corte = random.randint(0,len(self.pecas)-1)
			peca = random.randint(0,len(self.pecas)-1)
			self.geracao[i][corte] = peca
			self.pesos[i][peca] = random.randint(0,self.pecas[corte][2])
			pass
		pass

	def crossover(self):
		crossovers =  random.sample(range(0, self.populacao), int(self.ratecrossover * self.populacao))
		for i in range(0, len(crossovers), 2):
			corte = random.randint(1, int(len(self.pecas)*0.3))
			pai =  crossovers[i]
			mae =  crossovers[i+1]
			filho1 = self.geracao[pai][0:corte] + self.geracao[mae][corte:len(self.pecas)]+[0]
			filho2 = self.geracao[mae][0:corte] + self.geracao[pai][corte:len(self.pecas)]+[0]
			pesofilho1 = self.pesos[pai][0:corte] + self.pesos[mae][corte:len(self.pecas)]
			pesofilho2 = self.pesos[mae][0:corte] + self.pesos[pai][corte:len(self.pecas)]
			self.geracao[pai] = filho1
			self.geracao[mae] = filho2
			self.pesos[pai] = pesofilho1
			self.pesos[mae] = pesofilho2
			pass
		pass

	def roulette(self):
		tabelaprobabalidade = dict()
		acumulado = 0
		soma = np.sum(np.matrix(self.geracao)[:,len(self.pecas)])
		
		for i in range(0, self.populacao):
			resultado = float(self.geracao[i][len(self.pecas)]) / float(soma)
			acumulado+=resultado*100
			tabelaprobabalidade[i] = round(acumulado, 2)
		pass

		newgeracao = []
		for i in range(0, self.populacao):
			sorteio = round(random.random(), 2)*100
			anterior = 0
			if sorteio == 0:
				newgeracao.append(self.geracao[0])
			for j in range(0, len(tabelaprobabalidade)):
				if anterior < sorteio and sorteio <= tabelaprobabalidade[j]:
					newgeracao.append(self.geracao[j])
				anterior = tabelaprobabalidade[j]
		self.geracao = newgeracao
	
	def tournament(self):
		newgeracao = []
		limite = 0.85
		for i in range(0, self.populacao):
			sorteio = random.sample(range(0, self.populacao), 2)
			rand = random.random()
			if self.geracao[sorteio[0]][len(self.pecas)] < self.geracao[sorteio[1]][len(self.pecas)]:
				melhor = self.geracao[sorteio[0]]
				pior = self.geracao[sorteio[1]]
			else:
				melhor = self.geracao[sorteio[1]]
				pior = self.geracao[sorteio[0]]
			if rand <= limite:
				newgeracao.append(melhor)
			else:
				newgeracao.append(pior)
		self.geracao = newgeracao

	def evaluation(self):
		menorgeracao = self.solucao['menor']
		for i in range(0,self.populacao):
			solucao = dict()
			lagurasolucao = 0
			indice = 0
			maioraltura = 0
			alturaplaca = self.placa[1]
			larguraplaca = self.placa[0]
			
			for x in range(0, len(self.geracao[i])-1):
				quantidadepeca = self.pesos[i][x]
				alturapeca = self.pecas[self.geracao[i][x]][1]
				largurapeca = self.pecas[self.geracao[i][x]][0]
				
				for z in range(0, quantidadepeca):
					if lagurasolucao + largurapeca > larguraplaca:
						lagurasolucao = 0
						indice+=1
						alturaplaca = alturaplaca - maioraltura
						maioraltura = 0	

					if lagurasolucao + largurapeca <= larguraplaca and alturaplaca >= 0 and alturapeca < alturaplaca:
						lagurasolucao+=largurapeca
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

			self.geracao[i][len(self.geracao[i])-1] = perca
			if perca < self.solucao['menor']:
				self.solucao['menor'] = perca
				self.solucao['pecas'] = solucao
				self.solucao['cromossomo'] = self.geracao[i][0:len(self.pecas)]
				self.solucao['peso'] = self.pesos[i]
		self.percas.append(self.solucao['menor'])
		
		if menorgeracao == self.solucao['menor']:
			self.execucao +=1
		else:
			self.execucao = 0
		pass