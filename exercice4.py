import numpy as np
import matplotlib.pyplot as plt
from math import *

def f(x):
	return x**3-9*x**2+18*x-6
	
def tracer(f, abscisse_min, abscisse_max, titre):
	x = np.arange(abscisse_min,abscisse_max,0.01)
	courbe = plt.subplot(111)
	courbe.plot(x, f(x),'blue')
	courbe.grid(True)
	courbe.set_xlim(abscisse_min,abscisse_max)
	plt.title(titre)
	plt.show()

#pour afficher les valeurs de f pour un intervalle donnée
def afficher_fx(min,max):
	for i in range(min,max+1):
		print ("x=",i, "=> f(",i,")=",f(i))

def dichotomie(f, min, max):
	epsilon = pow(10,-3)
	nbre_iteration = 0
	while abs(max - min) > epsilon:
		m = (min+max)/2
		if f(min)*f(m) <= 0:
			max=m
		else:
			min=m
		nbre_iteration +=1
	print('la racine =',m)
	print("nombre d'iteration =",nbre_iteration)

def g(x):
	return 1/18*(6+9*x**2-x**3)

def point_fixe(g, x0, epsilon, nbre_max_iteration):
    iteration = 0
    xp = {}
    x = 0
    while (iteration < nbre_max_iteration):
	    try:
	        x = g(x0)
	    except OverflowError: 
	        break
	    xp[iteration] = x
	    if abs(x - x0) <= epsilon:
	        return xp,iteration
	    iteration += 1
	    x0 = x
    return "Aucun point fixe"
    
dichotomie(f,0,1)
dichotomie(f,2,3)
dichotomie(f,6,7)
x,iteration = point_fixe(g,1/2,pow(10,-3),100)
print("convergence point fixe :",x,"\nnombre ieration",iteration)
tracer(f,0,8,"courbe de f")
print("\n\t***********   END  ***************\n")
