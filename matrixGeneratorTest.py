import numpy as np

# Con esta funcion se genera la matriz A del problema, y el vector de terminos independientes
def generarMatrizSistEcuaciones(N, Ta, Tb, Tc, Td):
    dist = N - 1
    Naux = dist
    N = (N-1)*(N-1)

    
    matrizA = np.zeros((N,N))
    vectorB1 = np.zeros((N,1))
    vectorB2 = np.zeros((N,1))
    
    for i in range(N):
        for j in range(N):
            if(i == j):
                matrizA[i][j] = 4
                if( (j < N - 1) and ((j+1)%dist != 0) ):
                    matrizA[i][j+1] = -1
                if(j > 0 and (j%dist) != 0):
                    matrizA[i][j-1] = -1
                if(j + dist < N):
                   matrizA[i][j+dist] = -1
                if(j - dist >= 0):
                    matrizA[i][j-dist] = -1
                
    for i in range(0, Naux):
        vectorB1[i][0] = Ta

    for i in range(N-Naux, N):
        vectorB1[i][0] = Tb

    for i in range(0, N, Naux):
        vectorB2[i][0] = Tc

    for i in range(Naux-1, N, Naux):
        vectorB2[i][0] = Td

    vectorB = vectorB1 + vectorB2
   
    return matrizA, vectorB



N = 5
print('N = ', N)
matrizA, vectorB = generarMatrizSistEcuaciones(N, 1, 2, 3, 4)
#print(matrizA)
