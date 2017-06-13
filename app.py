from GA import GA

populacao = 100
mutation = 0.1
crossover = 0.25
instancias = [[120,10],[130,23],[100,12]]
placa = [250,250]

ga = GA(populacao, instancias, placa, mutation, crossover)
ga.duplique()
print ga.preprocessing()
print ga.generate()