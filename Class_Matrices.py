#Se creara la clase Matriz para todas las operaciones basicas relacionadas con matrices
#Esta clase hereda de Complejo que a su vez hereda de Fraccion
from Class_Complejos import Complejo
from Class_Fracciones import Fraccion  #Es mandada a llamar unicamente por la función isPar() y por pruebas()
import random
class Matriz(Complejo):
  def __init__(self,filas=0,columnas=0,tama=25):
    #super().__init__(tam=tama)  # Pasando tama a Complejo
    self.filas=filas
    self.columnas=columnas
    #self.tama=tama
    #print("inicializado",self.tama)
    self.matriz=[[Complejo() for _ in range(self.columnas) ] for _ in range(self.filas)]

  def __str__(self):
    return '\n'.join(' '.join(str(elemento) for elemento in fila) for fila in self.matriz)

  def ingresarMat(self):
    for i in range(self.filas):
      for j in range(self.columnas):
        print(f"[{i},{j}]",end=" ",sep=" ")
        self.matriz[i][j].inComp()
  def __add__(self,other):
    if isinstance (other,Matriz):
      if self.filas==other.filas and self.columnas==other.columnas:
        result=Matriz(self.filas,self.columnas)
        for i in range(self.filas):
          for j in range(self.columnas):
            result.matriz[i][j]=self.matriz[i][j]+other.matriz[i][j]

        return result
      else:
        raise ValueError("Las matrices no tienen las mismas dimensiones")
    return NotImplemented
  def __sub__ (self,other):
    if isinstance(other,Matriz):
      if self.filas==other.filas and self.columnas==other.columnas:
        result=Matriz(self.filas,self.columnas)
        for i in range(self.filas):
          for j in range(self.columnas):
            result.matriz[i][j]=self.matriz[i][j]-other.matriz[i][j]
        return result
      else:
        raise ValueError("Las matrices no tienen las mismas dimensiones")
    return NotImplemented
  def __mul__(self,other):
    if isinstance(other,Matriz):
      if self.columnas==other.filas:

        result=Matriz(self.filas,other.columnas,tama=100)
        for i in range(self.filas):
          for j in range (other.columnas):
            for k in range(self.columnas):
              #print(i+j+k)
              result.matriz[i][j]=result.matriz[i][j]+self.matriz[i][k]*other.matriz[k][j]
        return result
      else:
        raise ValueError("Las matrices no tienen las mismas dimensiones")
    return NotImplemented
  def pruebas(self):
    for i in range(self.filas):
      for j in range(self.columnas):
        #self.matriz[i][j]=Complejo(Fraccion(i+j,1),Fraccion())
        self.matriz[i][j]=Complejo(Fraccion(random.randint(-10,10),random.randint(1,5)),Fraccion(random.randint(-10,10),random.randint(1,5)))

  def detM(self):
    if self.filas==self.columnas:
      if self.filas==1:
        return self.matriz[0][0]
      elif self.filas==2:
        return self.matriz[0][0]*self.matriz[1][1] - self.matriz[0][1]*self.matriz[1][0]
      else:
        det=Complejo()
        for j in range(self.columnas):
          det+=self.isPar(j)*self.matriz[0][j]*self.mMenor(0,j).detM()
        return det
    else:
      raise ValueError("La matriz no es cuadrada")
  def detM_dec(self):
    return self.detM().dec()


  def mMenor(self, fila, columna):
      if fila >= self.filas or columna >= self.columnas:
          raise ValueError("Fila o columna fuera de los límites")
      menor = Matriz(self.filas - 1, self.columnas - 1)

      for i in range(self.filas):
          for j in range(self.columnas):
              if i != fila and j != columna:
                  nueva_fila = i if i < fila else i - 1
                  nueva_columna = j if j < columna else j - 1
                  menor.matriz[nueva_fila][nueva_columna] = self.matriz[i][j]
      return menor


  def isPar(self,num):
    if num%2==0:
      return Complejo(Fraccion(1,1),Fraccion(0,1))
    else:
      return Complejo(Fraccion(-1,1),Fraccion(0,1))