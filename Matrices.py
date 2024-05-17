# Algebra Lineal con Numpy para lo cual usaremos el submodulo "linalg"
# Si queremos calcular la Traza de la Matriz usaremos el metodo "trace()" 
import numpy as np
m1 = np.array([[1, 2, 2, 3], [1, 0, -2, 0], [3, -1, 1, -2], [4, -3, 0, 2]])
Y = np.trace(m1)
print("La traza de la matriz m es {}".format(Y))
# En este caso estamos usando la funcion "f-string"
print(f"La traza de la matriz m es {Y}") 

# Si queremos convertir una matriz en una matriz triangular superior usamos el metodo "triu()"
import numpy as np
m1 = np.array([[1,2,2,3],[1,0,-2,0],[3,-1,1,-2],[4,-3,0,2]])
Z = np.triu(m1, k=0)
print(Z)

# Multiplicaremos dos matrices de orden 3 usando el metodo"matmul()

import numpy as np
A = np.array([[4,3,2],[5,1,9]])
B = np.array([[5,4,1],[7,9,3],[2,1,2]]) 
C = np.matmul(A,B)
print(C)

# Si queremos calcular el producto interno de elementos de mismo indice de dos matrices usaremos el metodo "inner()"

import numpy as np
A1 = np.array([[4,3,2]])
B1 = np.array([[5,4,1]]) 
C1 = np.inner(A1,B1)
print(C1)

# Para Hallar la potencia de una matriz cuadrada usaremos el metodo "matrix_power(m,n)" donde "m" es la matriz y "n" es la potencia al cual estamos elevando la matriz
import numpy as np
from numpy.linalg import matrix_power
A2 = np.array([[0,7,8],[0,0,3],[0,0,0]])
B2 = np.linalg.matrix_power(A2,3) # La matriz A2 lo elevaremos a la potencia 3
print(B2)

# Calcularemos la determinate de una matriz usando el metodo "det()"
import numpy as np
m1 = np.array([[1,2,2,3],[1,0,-2,0],[3,-1,1,-2],[4,-3,0,2]])
X = np.linalg.det(m1)
print(X)

# Calcularemos la inversa de una matriz usando el metodo "inv()"
import numpy as np
from numpy.linalg import inv
m2 = np.array([[1,1,1],[1,2,3],[1,3,4]])
X1 = inv(np.matrix(m2))
print(X1)




