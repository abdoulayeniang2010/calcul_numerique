import numpy as np
#********les donnees*******************
B = np.array([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4],
])
A = np.array([
    [1, 0.5, 0],
    [0, 2, 1],
    [-1, 1, 1],
])
b = np.array([2,5,2])
#**************************************

D = np.diag(np.diag(B))
E = D-np.tril(B,0)
F = D-np.triu(B,0)
#inverse de la matrice diagonale D
D1 = np.linalg.inv(D) 
print("\n\t********************************************************\n")
# Jacobi est le produit de D1 et la somme de E+F
jacobi =D1.dot(E+F)
print("la matrice de Jacobi\n",jacobi)
#liste des valeurs propres 
spectre_jacobi = np.linalg.eig(jacobi)[0]
print("les valeurs propres de Jacobi\n\t",spectre_jacobi)
#le rayon spectral de jacobi = Rho 
rho_Jacobi = abs(max(spectre_jacobi))
print("le rayon de spectre de Jacobi =",rho_Jacobi)
if rho_Jacobi < 1:
	print("\n\tla methode converge avec Jacobi")

print("\n\t********************************************************\n")
#Methode de Gauss Seidel
inverse_DE = np.linalg.inv(D-E)
gauss = inverse_DE.dot(F)
print("la matrice de Gauss Seidel\n",gauss)
spectre_gauss_seidel = np.linalg.eig(gauss)[0]
print("les valeurs propres Gauss Seidel\n\t",spectre_gauss_seidel)
rho_gauss_seidel = abs(max(spectre_gauss_seidel))
print("le rayon de spectre de Gauss Seidel =",rho_gauss_seidel)
if rho_gauss_seidel < 1:
    print("\n\tla methode converge avec Gauss Seidel")

print("\n\t********************************************************\n")
#la methode qui converge le plus rapidement entre Jacobi et Seidel
if rho_Jacobi > rho_gauss_seidel:
    print("Gauss Seidel converge plus vite que Jacobi")
else:
    print("Jacobi converge plus vite que Gauss Seidel")

#Resolution de Jacobi
def solution_jacobi(A,b,nbre_max_iteration,tolerance):
	if 0 in np.diag(A):
		print("il y a un zero sur la diagonale")
	D = np.diag(np.diag(A))#matrice diagonale de A
	E = D-np.tril(A)
	F = D-np.triu(A)
	v = b
	iteration = 0 #initialisation iteration
	convergence = 0 #pas de convergence
	for i in range (int(nbre_max_iteration)):
		v = np.linalg.inv(D).dot((E+F).dot(v)+b)
		if max(abs(A.dot(v)-b)) < tolerance:
			convergence = 1
			iteration = i
			break
	print(" la solution de l'equation par la methode de Jacobi est\n\t ",v)
	print("nombre iteration =",iteration)
 
def solution_gauss_seidel(A,b,nbre_max_iteration,tolerance):
	if 0 in np.diag(A):
		print("il y a un zero sur la diagonale")
	D = np.diag(np.diag(A))#matrice diagonale de A
	E = D-np.tril(A)
	F = D-np.triu(A)
	v = b
	iteration = 0 #initialisation iteration
	convergence = 0 #pas de convergence
	for i in range (int(nbre_max_iteration)):
		v = np.linalg.inv(D-E).dot((F).dot(v)+b)
		if max(abs(A.dot(v)-b)) < tolerance:
			convergence = 1
			iteration = i
			break
	print(" la solution de l'equation par la methode de Gauss Seidel est \n\t",v)
	print("nombre iteration =",iteration)

print("\n\t************ Resolution avec Jacobi  *******************\n")
solution_jacobi(A,b,pow(10,4),pow(10,-5))
print("\n\t************ Resolution avec Gauss Seidel  **************\n")
solution_gauss_seidel(A,b,pow(10,4),pow(10,-5))
print("\n\t\t************* End ****************\n")
