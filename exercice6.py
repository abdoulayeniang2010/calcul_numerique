#import numpy as np
#import matplotlib as plt
from pylab import *

a = 0
b = 2*pi
n = 100
i_exact = -1*float(0.122122604618968)


def f(x):
	return x*exp(-x)*cos(2*x)



def point_milieu(f, a, b, n):
    somme = 0
    pas = (b - a) / n
    x = a 
    for i in range(0, n):
        somme += f((x+(x+pas))/2)
        x += pas
    return somme * pas

    
def simpson(f, a, b, n):
    pas = (b - a) / n
    somme = (f(a) + f(b)) / 2 + 2 * f(a + pas / 2)  # On initialise la somme
    x = a + pas
    for i in range(1, n):
        somme += f(x) + 2 * f(x + pas / 2)
        x += pas
    return somme * pas / 3

    
def trapeze(f, a, b, n):
    somme = (f(a) + f(b)) / 2   
    pas = (b - a) / n
    x = a + pas
    for i in range(1, n):
        somme += f(x)
        x += pas
    return somme * pas


def tracer_aire(f,a,b,n):
	x = linspace(a,b,n)
	y = f(x)
	courbe = subplot(111)
	courbe.plot(x,y,'ob-',color="red")
	courbe.set_xlim(0)
	#tracer les petits rectangles 
	for i in range(n-1):
		x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]]
		y_rect = [0   , y[i], y[i]  , 0     , 0   ]
		courbe.plot(x_rect, y_rect,'r',color="green")
	plt.show()


print("Methode du Point Milieu I(f) =",point_milieu(f,a,b,n))
print("Methode de Simpson I(f) =",simpson(f,a,b,n))
print("Methode de Trapeze I(f) =",trapeze(f,a,b,n))


print("\n****************************************\n")

print("Erreur Methode Point milieu si n augmente")
print("n = 150 :",abs(i_exact - point_milieu(f,a,b,150)))
print("n = 200 :",abs(i_exact - point_milieu(f,a,b,200)))
print("n = 250 :",abs(i_exact - point_milieu(f,a,b,250)))
print("\n*******************************************")

print("Erreur Methode Trapeze si n augmente")
print("n = 150 :",abs(i_exact - trapeze(f,a,b,150)))
print("n = 200 :",abs(i_exact - trapeze(f,a,b,200)))
print("n = 250 :",abs(i_exact - trapeze(f,a,b,250)))
print("\n*******************************************")

print("Erreur Methode Simpson si n augmente")
print("n = 150 :",abs(i_exact - simpson(f,a,b,150)))
print("n = 200 :",abs(i_exact - simpson(f,a,b,200)))
print("n = 250 :",abs(i_exact - simpson(f,a,b,250)))

tracer_aire(f,a,b,n)
print("\n\t********* Fin du programme ************")
