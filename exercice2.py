import math
import numpy as np
A1 = [
    [2,4,-4,1],
    [3,6,1,-2],
    [-1,1,2,3],
    [1,1,4,1]
    ]
    
b1 = [1,1,1,2]

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def determinant_mineur(A):
       for i in range(len(A)):
            for j in range(len(A)):
                C = getMatrixMinor(A, i, j)
                print("det =", np.linalg.det(C))
                
                 
determinant_mineur(A1)                 

A = [ 
    [4,0,2,0],
    [0,4,0,2],
    [2,0,5,0],
    [0,2,0,5]
    ]
    
b = [1,2,1,3]
def symmetric(A):   #Check if given matrix is symmetrical
    n=len(A)                                
    B=[[0.0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]

    #Checks if given matrix and its transpose are equal
    for i in range(n):
        for j in range(n):
            if( A[i][j] != B[i][j] ):
                return False
    return True
           

def choleskyDecomposition(A):  #Performs a Cholesky Decomposition of a matrix and returns a lower triangular matrix
    n = len(A)
    L = [[0.0] * n for i in range(n)] #Creates a zero matrix

    if symmetric(A):
        for i in range(n):
            for j in range(i+1):
                suma = sum( L[i][k] * L[j][k] for k in range(j))
                if (i == j):
                    L[i][j] = math.sqrt( A[i][i] - suma)
                else:
                    L[i][j] = (1.0 / L[j][j] * ( A[i][j] - suma) )
    return L

def transpose(A): #Returns a transpose of a given matrix
    return [ [A[j][i] for j in range(len(A)) ] for i in range (len(A[0])) ]

def fwdSubstitution(A,b):   #Performs a forward substitution,solves the equation Ly=b
    n = len(A)
    y = [0 for i in range(n)]

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] = y[i] - A[i][j]*y[j]
        y[i] = y[i]/A[i][i]

    return y

def backSubstitution(A,b):  #Performs a backwards substitution,solves LTx=y, returns the solution of Ax=b
    n = len(A)
    x = [0 for i in range(n)]
    x[n-1] = b[n-1] / A[n-1][n-1]

    for i in range(n-2,-1,-1):
        suma = b[i]
        for j in range(i+1,n):
            suma = suma - A[i][j]*x[j]
        x[i] = suma/A[i][i]
    return x

def choleskyFactorisation(A,b):
    L = choleskyDecomposition(A)
    Lt = transpose(L)
    y = fwdSubstitution(L,b)
    x = backSubstitution(Lt,y)
    return x

print("La solution par Methode de Cholesky")
print(choleskyFactorisation(A,b))