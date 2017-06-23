from GA import GA
from instances import Instances
from graphs import Graphs
import time

instances = Instances()
instances.process()

inicio =  time.time()
execucao = 400
instancia = 0
populacao = 200
mutation = 0.01
crossover = 0.4

instancias = instances.instances[instancia]['pecas']
placa = instances.instances[instancia]['placa']

ga = GA(populacao, instancias, placa, mutation, crossover)
ga.duplique()
#ga.pecas = instancias
ga.preprocessing()
ga.generate()

while ga.execucao <=execucao:
    ga.evaluation()
    ga.roulette()
    #ga.tournament()
    ga.crossover()
    ga.mutation()

fim = time.time()
print fim - inicio
print ga.solucao

graphs = Graphs(ga, placa)
graphs.plotgraphs()
