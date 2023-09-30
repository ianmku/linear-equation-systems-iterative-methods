import numpy as np

def jacobiMethod(A, b, xSeed, tolerance):
 
    diagonalElements = A.diagonal()
    D = np.diagflat(diagonalElements)
    Dinv = np.linalg.inv(D)
    L = -1*(np.tril(A) - D)
    U = -1*(np.triu(A) - D)
    sumLU = L + U
    e = np.matmul(Dinv, b)
    T = np.matmul(Dinv, sumLU)
    
    x = calculateNewSolution(xSeed, b, e, T)
    r = calculateNewError(x, xSeed)
    timesIterated = 1
    print(x)
    print(r)


    while( r > tolerance):
        timesIterated += 1
        previousSolution = x
        x = calculateNewSolution(previousSolution, b, e, T)
        
        r = calculateNewError(x, previousSolution) * 100

        print('New solution is: ', x, 'error: ', r, 'iteration number: ', timesIterated)
        

    print('Solution is', x)
    #print('Times iterated:', timesIterated)

def calculateNewSolution(previousSolution, b, e, T):
    return (np.matmul(T, previousSolution) + e)

def calculateNewError(currentSolution, previousSolution):
    
    return ( (np.linalg.norm(currentSolution-previousSolution, np.inf)) / np.linalg.norm(currentSolution, np.inf)) 

def jacobiMethod2(A, b, xSeed, tolerance, maxIterations):
    
    matrixDimension = len(A)
    currentSolution = xSeed.copy()
    newSolution = xSeed.copy()
    
    for iterationCount in range(maxIterations):
        for i in range(matrixDimension):
            summation = sum(A[i][j] * currentSolution[j] for j in range(matrixDimension) if j != i)
            newSolution = (b[i] - summation) / A[i][i]
            print(newSolution)
            #max(abs(newSolution[i] - currentSolution[i]) for i in range(matrixDimension)) < tolerance

        if(True == False):
            return newSolution 
        
        currentSolution = newSolution    

    return -1
A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]])
b = np.array([24, 30, -24])
xSeed = np.array([0, 0, 0])

jacobiMethod(A, b, xSeed, 0.1)
#jacobiMethod2(A, b, xSeed, 0.1, 1000)
