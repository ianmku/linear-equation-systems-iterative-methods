import numpy as np
import matplotlib.pyplot as plt

def sor(A, b, xSeed, maxIterations, tolerance, omega):
   
    matrixDimension = len(A)
    currentSolution = xSeed.copy()
    newSolution = xSeed.copy()

    for iterationCount in range(maxIterations):
         
        for i in range(matrixDimension):
           
            summationOne = 0
            summationTwo = 0
            

            for j in range(i+1 ,matrixDimension):
                
                if A[i][j] != 0:
                    summationOne += A[i][j] * newSolution[j]
                    
                
            if(i != 0):
                for j in range(0, i):
                    
                    if A[i][j] != 0:
                        summationTwo +=  A[i][j] * newSolution[j]
                        
    
            
            newSolution[i] = (b[i] - summationOne - summationTwo) * (omega / A[i][i]) + (1-omega) * newSolution[i]
        
        
        error = ( np.linalg.norm(np.array(newSolution)-np.array(currentSolution)) / np.linalg.norm(np.array(newSolution))) * 100
        
        
        
        if error < tolerance:
            break
        currentSolution = newSolution.copy()
        

    return newSolution, iterationCount + 1, error

def generarMatrizSistEcuaciones(N, Ta, Tb, Tc, Td):
    #Ta = Twest
    #Tb = Teast
    #Tc = TSouth
    #Td = Tnorth

    dist = N - 1
    Naux = dist
    N = (N-1)*(N-1)

    #Las matrices A y B se generan a partir del valor de N, segun se observo como va tomando su forma a medida que N cambia

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


def aplicarFuncion(iteraciones, R):
    return pow(R, 1/iteraciones)

def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='cool')
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            plt.text(x, y, '%.2f' % arr[y, x],
                     horizontalalignment='center'
                     )
    plt.colorbar()
    plt.show()

#------------------------------------------------------------#

N = 8 #Cambiar segun el caso
matrizA, vectorB = generarMatrizSistEcuaciones(N, 50, 90, 90, 10) #Cambiar segun el caso
semilla = np.zeros(((N-1)*(N-1), 1))
omegas = np.arange(1.00, 2.00, 0.05)

auxOmega = []
auxIteraciones = []
estimacionEmpirica = []

# Esto lo utilizamos para los casos de la primera parte, donde necesitamos que omega vaya variando
#for omega in omegas:
#    solucion, iteraciones, error = sor(matrizA, vectorB, semilla, 1000, 0.01, omega)
#    aux = [iteraciones, error]
#    
#    auxOmega.append(omega)
#    auxIteraciones.append(iteraciones)
    

#Esto se utiliza para graficar en la 2da parte del TP, donde N=8
Wopt = 1.446
solucion, iteraciones, error = sor(matrizA, vectorB, semilla, 1000, 0.001, Wopt)
heatMap = np.zeros((N-1, N-1))
posicionVector = 0
for i in range(0, N-1):
    for j in range(0, N-1):
        elementoVector = solucion[posicionVector] 
        heatMap[i][j] = elementoVector
        posicionVector += 1


print('El vector solucion es: ', solucion)

heatmap2d(heatMap)


#Esto tambien se utilizo para los incisos en que N=4 y N=32
#estimacionEmpirica = [aplicarFuncion(iteraciones, 0.01) for iteraciones in auxIteraciones]

#plt.plot(auxIteraciones, auxOmega, label = "iter")
#plt.plot()
#plt.scatter(auxIteraciones, estimacionEmpirica, label = "PTsor")


#plt.show()



