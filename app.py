from GA import GA

populacao = 100
mutation = 0.1
crossover = 0.25
instancias = [
    [167,184],
    [114,118],
    [167,152],
    [83,140],
    [70,86],
    [143,166],
    [120,160],
    [66,148],
    [87,141],
    [69,165]
]
placa = [250,250]

ga = GA(populacao, instancias, placa, mutation, crossover)
ga.duplique()
ga.preprocessing()
ga.generate()
ga.evaluation()