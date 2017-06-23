from GA import GA
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

class Graphs(object):
	def __init__(self, ga, placa):
		self.ga = ga
		self.placa = placa

	def plotgraphs(self):
		plt.plot(self.ga.percas)
		altura = 0
		fig = plt.figure()
		ax = fig.add_subplot(111)
		codes = [
		    Path.MOVETO,
		    Path.LINETO,
		    Path.LINETO,
		    Path.LINETO,
		    Path.CLOSEPOLY,
		]
		for i in self.ga.solucao['pecas']:
		    maioraltura = 0
		    largura = 0
		    for j in self.ga.solucao['pecas'][i]:
		        if j[1] > maioraltura:
		            maioraltura = j[1]
		        verts = [
		            (largura, altura), 
		            (largura, j[1]+altura),
		            (largura+j[0], j[1]+altura), 
		            (largura+j[0], altura), 
		            (0, 0), 
		        ]
		        largura += j[0]
		        path = Path(verts, codes)
		        patch = patches.PathPatch(path, facecolor='blue', lw=2)
		        ax.add_patch(patch)
		    pass
		    altura += maioraltura
		ax.set_xlim(0,self.placa[0])
		ax.set_ylim(0,self.placa[1])
		plt.show()