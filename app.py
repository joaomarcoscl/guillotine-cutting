#coding=utf8
from GA import GA
from instances import Instances
from graphs import Graphs
import time

instancia = 'cut1' #escolher nome do arquivo na pasta instances. OBS: sem o '.txt'
instances = Instances()
instances.files.append(instancia)
instances.process()
file = open('results.txt', 'w')

execucao = 5000 #limite de mudanças no resultado
populacao = 100
mutation = 0.02
crossover = 0.4


for i in range(0, 10):
    inicio =  time.time()
    instancias = instances.instances[0]['pecas']
    placa = instances.instances[0]['placa']

    ga = GA(populacao, instancias, placa, mutation, crossover)
    ga.duplique()
    ga.preprocessing()
    ga.generate()

    while ga.execucao <=execucao:
        ga.evaluation()#selecao 1
        #ga.roulette() #selecao 2
        ga.tournament()
        ga.crossover()
        ga.mutation()

    fim = time.time()
    file.write('Instancia: '+instances.files[0]+' - Interação: '+str(i)+'\n')
    file.write('Tempo: '+str(fim - inicio)+'\n')
    file.write('Perca: '+str(ga.solucao['menor']*100)+'\n')
    file.write('Pecas: '+str(ga.solucao['pecas'])+'\n')
    file.write('Cromossomo: '+str(ga.solucao['cromossomo'])+'\n')
    file.write('Peso: '+str(ga.solucao['peso'])+'\n\n\n\n\n')
    graphs = Graphs(ga, placa, instances.files[0]+'-'+'interação-'+str(i))
    graphs.plotgraphs()
pass
file.close()