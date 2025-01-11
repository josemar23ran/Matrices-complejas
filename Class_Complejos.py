#Esta es la clase complejo, la cual estara preparada para trabajar con numeros enteros como fracciones
from Class_Fracciones import Fraccion

class Complejo(Fraccion):
  def __init__(self,real=Fraccion(),img=Fraccion()):
    #self.tam=tam
    self.real=real
    self.real.simplificar()
    self.img=img
    self.img.simplificar()
  def dec(self):
    real = format(self.real.dec(), '.3f')  # Formatea el número real
    img = format(self.img.dec(), '.3f')    # Formatea el número imaginario
    if self.img.dec()>=0:
      return f"{real}+{img}i"
    else:
      return f"{real}{img}i"
  def __str__(self):
      width = 27  # Ancho total deseado para cada impresión
      real_str = str(self.real)
      img_str = str(self.img)
      if self.img != 0 and self.real != 0:
          if self.img == 1:
              return f"{(real_str + ' + i').ljust(width)}"
          elif self.img == -1:
              return f"{(real_str + ' - i').ljust(width)}"
          elif self.img > 0:
              return f"{(real_str + ' + ' + img_str + 'i').ljust(width)}"
          else:
              return f"{(real_str + ' - ' + str(abs(self.img)) + 'i').ljust(width)}"
      elif self.real == 0 and self.img == 0:
          return f"{'0'.ljust(width)}"
      elif self.img == 0:
          return f"{real_str.ljust(width)}"
      else:
          if self.img == 1:
              return f"{'i'.ljust(width)}"
          elif self.img == -1:
              return f"{'- i'.ljust(width)}"
          else:
              return f"{(img_str + 'i').ljust(width)}"

  def __add__(self,other):
    if isinstance(other,Complejo):
      preal=self.real + other.real
      pimg =self.img + other.img
      result=Complejo(preal,pimg)
      return result
    return NotImplemented
  def __sub__(self,other):
    if isinstance(other,Complejo):
      preal=self.real - other.real
      pimg =self.img - other.img
      result=Complejo(preal,pimg)
      return result
    return NotImplemented
  def __mul__(self,other):
    if isinstance (other,Complejo):
      preal=self.real*other.real-self.img*other.img
      pimg=self.real*other.img+self.img*other.real
      result=Complejo(preal,pimg)
      return result
    elif isinstance(other,int):
      preal=self.real*other
      pimg=self.img*other
      result=Complejo(preal,pimg)
      return result
    return NotImplemented
  def conj(self):
    neg=Fraccion(-1,1)
    return Complejo(self.real,neg*self.img)

  def __truediv__(self,other):
    if isinstance (other,Complejo):
      preal=(self.real*other.real+self.img*other.img)/(other.real**2+other.img**2)
      pimg=(self.img*other.real-self.real*other.img)/(other.real**2+other.img**2)
      result=Complejo(preal,pimg)
      return result
    return NotImplemented

  def inComp(self):
    while(True):
      print("Ingresa el numero (Complejo,entero y/o Fraccion)",end="",sep=" ")
      cna=input()
      real=0
      img=0
      cna2=cna.replace(" ","")
      permitidos = "0123456789i/+-."
      es_valido = all(caracter in permitidos for caracter in cna2)
      if not es_valido:   #solo se valida que no entren otros caracteres
          print("Entrada no valida, vuelve a ingresarla")
          continue
      if cna2[0]=="+":
        cna2=cna2[1:]
      if "i" in cna2:
        index_i=cna2.index("i")
        img=cna2[:index_i]
        if "+" in img:
          aux=img.split("+")
          real=aux[0]
          img=aux[1]
        elif "-" in img and img[0]!="-":
          aux=img.split("-")
          real=aux[0]
          img="-"+aux[1]
        elif "-" in img and img[0]=="-" and img.count("-")==2:
          aux=img.split("-")
          real="-"+ aux[-2]
          img="-" + aux[-1]
        if cna2[index_i-1]=="-" :
          img="-1"
        elif cna2[index_i-1]=="+" :
          img="1"
      else:
        real=cna2
      self.real=Fraccion()
      self.img=Fraccion()
      if self.real.inFrac(real) and self.img.inFrac(img):
        break
      else:
        print("No es un numero valido! ")
        continue