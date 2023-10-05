import numpy as np
import regex as re


#Con esto se genera la matriz completa, con la temperatura de los bordes para poder aplicar el operador
def generarMatriz(cantidadLadosIguales):
    
    N = cantidadLadosIguales + 1
    
    matriz = []
    
    for i in range(N):
        row = []
        for j in range(N):
            if(i==0):
                row.append('Tno')
            elif(j==0):
                row.append('Twe')
            elif(i==N-1):
                row.append('Tso')
            elif(j==N-1):
                row.append('Tea')
            else:
                row.append('x'+str(i)+str(j))
        matriz.append(row)
        print(row)
    return matriz
    
#Esta funcion es para aplicar el operador sobre los elementos de la matriz completa con el contorno con temperaturas fijas, generando el sistema de ecuaciones
#para poder visualizarlo
def aplicarOperador(matriz, i, j):
    #if (i != 0 or i != 4 or j !=0 or j != 4):
    terminosAExaminar = [matriz[i-1][j], matriz[i+1][j], matriz[i][j-1], matriz[i][j+1]]
    terminosLadoIzq = []
    terminosLadoDer = []

    terminosLadoIzq.append('4*' + matriz[i][j])

    for termino in terminosAExaminar:
        if(esTerminoIndependiente(termino)):
            terminosLadoDer.append('+1*'+termino)
        else:
            terminosLadoIzq.append('-1*'+termino)

    if len(terminosLadoDer) == 0:
        terminosLadoDer.append('0')
    
    ecuacion = ''.join(terminosLadoIzq)+'=                  '+''.join(terminosLadoDer)
    #for termino in terminosLadoIzq:
    ecuacion.join(terminosLadoIzq)
    #ecuacion = '4*' + matriz[i][j] + ' - ' + matriz[i-1][j] + ' - ' + matriz[i+1][j] + ' - ' + matriz[i][j-1] + ' - ' + matriz[i][j+1] + ' = 0'
    #print('terminos: ', terminos)
    #print(terminosLadoIzq)
    #print('=')
    #print(terminosLadoDer)
    print(ecuacion)
    return ecuacion

def esTerminoIndependiente(termino):
    return ('T' in termino)

def generarSistemaDeEcuaciones(matriz):
    ecuaciones = []
    for i in range(1, len(matriz)-1):
        for j in range(1, len(matriz)-1):
            ecuacion = aplicarOperador(matriz, i, j)
            #print(ecuacion)
            ecuaciones.append(ecuacion)
    return ecuaciones
    
matriz = generarMatriz(5)
print('--------------------------------------------------')
ecuaciones = generarSistemaDeEcuaciones(matriz)
