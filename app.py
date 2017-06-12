from GA import GA

populacao = 10
limite = 10
instancias = [[120,10],[130,23],[100,12]]
placa = [250,250]

ga = GA(populacao, limite, instancias, placa)
ga.duplique()
ga.preprocessing()
print ga.generate()