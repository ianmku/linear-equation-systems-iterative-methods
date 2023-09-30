import numpy as np
def jacobi(A, b, x0, tol=0.1, max_iter=1000):
    matrixDimension = len(A)
    currentSolution = x0.copy()
    newSolution = x0.copy()

    for iterationCount in range(max_iter):
        #print(iter_count)
        for i in range(matrixDimension):
            summation = sum(A[i][j] * currentSolution[j] for j in range(matrixDimension) if j != i)
            newSolution[i] = (b[i] - summation) / A[i][i]

        # Check for convergence
        error = ( max(abs(newSolution[i] - currentSolution[i]) for i in range(matrixDimension)) / max(abs(newSolution[i]) for i in range(matrixDimension)) ) * 100
        print('parte de arriba: ', max(abs(newSolution[i] - currentSolution[i]) for i in range(matrixDimension)))
        print("Iteration: ", iterationCount, "error: ", error)
        if error < tol:
            print('Error: ', error)
            print(newSolution)
            return newSolution

        currentSolution = newSolution.copy()

    
    raise Exception("Jacobi method did not converge")

# Example usage:
A = [[4, 3, 0], [3, 4, -1], [0, -1, 4]]

b = [24, 30, -24]


x0 = [0, 0, 0]

solution = jacobi(A, b, x0)
print("Solution:", solution)
