from Class_Matrices import Matriz
#Ejemplo de uso, el metodo pruebas sirve para rellenar con numeros aleatorios la matriz de tamaño n, 
# asegurandose de no ser llenada con una fraccion erronea
print("Inicio de pruebas ")
print("\nMatriz A: ")
A=Matriz(4,4)
A.pruebas()
print(A)
print("Determinante de A: ",A.detM_dec())

print("\nMatriz B: ")
B=Matriz(4,4)
B.pruebas()
print(B)
print("Determinante de B: ",B.detM_dec())

print("A + B = \n",A+B)
print("\nA - B = \n",A-B)
print("\nA * B = \n",A*B)

