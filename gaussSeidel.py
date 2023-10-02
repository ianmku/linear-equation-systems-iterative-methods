def gauss_seidel(A, b, xSeed, maxIterations, tolerance):
   
    matrixDimension = len(A)
    currentSolution = xSeed.copy()
    newSolution = xSeed.copy()

    for iterationCount in range(maxIterations):
        max_diff = 0.0  # Initialize123 the maximum difference for this iteration
        print('La solucion actualmente vale: ', currentSolution)
        for i in range(matrixDimension):
            # Calculate the new value for x[i] using the Gauss-Seidel formula
            summationOne = 0
            summationTwo = 0
            print('X', i+1, '= ', end=' ')

            for j in range(i+1 ,matrixDimension):
                print('A', i+1, j+1, '=', A[i][j], ' * ', currentSolution[j], end=' ')
                summationOne += A[i][j] * newSolution[j]
            print('F1S', end=' ')

            if(i == 0):
                print(' ')
            if(i != 0):
                for j in range(0, i):
                    print('A', i+1, j+1, '=', A[i][j],' * ', newSolution[j], end=' ')
                    summationTwo +=  A[i][j] * newSolution[j]
                print('F2S')

            # Update the solution vector
            newSolution[i] = (b[i] - summationOne - summationTwo) / A[i][i]

        # Check the convergence for this variable
        error = ( max(abs(newSolution[i] - currentSolution[i]) for i in range(matrixDimension)) / max(abs(newSolution[i]) for i in range(matrixDimension)) ) * 100
        print(error)
        # Check for convergence based on the maximum difference in this iteration
        if error < tolerance:
            break
        currentSolution = newSolution.copy()
        

    return newSolution, iterationCount + 1

# Example usage:
coeff_matrix = [[4, 3, 0], [3, 4, -1], [0, -1, 4]]
constants = [24, 30, -24]
initial_guess = [0, 0, 0]

solution, iterations = gauss_seidel(coeff_matrix, constants, initial_guess, 100, 0.1)
print("Solution:", solution)
print("Iterations:", iterations)
