import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**3-9*x**2+18*x-6
	
def tracer(f, abscisse_min, abscisse_max, titre):
	x = np.arange(abscisse_min,abscisse_max,0.01)
	courbe = plt.subplot(111)
	courbe.plot(x, f(x),'blue')
	courbe.grid(True)
	courbe.set_xlim(abscisse_min,abscisse_max)
	courbe.set_ylim(0,) #démarrer l'axe des ordonnées a zero
	plt.title(titre) 
	plt.show()

tracer(f,0,8,"graphe exercice 4 pour f(x) >= 0")
