import numpy as np

def jacobiMethod(A, b, xSeed, n):
    # A = D + L + U, 
    diagonalElements = A.diagonal()
    D = np.diagflat(diagonalElements)
    Dinv = np.linalg.inv(D)
    L = -1*(np.tril(A) - D)
    U = -1*(np.triu(A) - D)
    sumLU = L + U
    
    x = (np.matmul(Dinv, np.matmul(sumLU, xSeed)) + np.matmul(Dinv, b))

    print(x)

A = np.array([[10, 2, 6], [1, 10, 4], [2, -7, -10]])
b = np.array([28, 7, -17])
xSeed = np.array([1, 2, 3])

jacobiMethod(A, b, xSeed, 1)
