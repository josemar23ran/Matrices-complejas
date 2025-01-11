#Primero se define la clase Fracción la cual tendra todas nuestras funciones
#relaccionadas con las fracciones
class Fraccion:
  def __init__(self,num=0,den=1):
    self.num=num
    self.den=den
    self.cadena=""
    self.simplificar()

  def impFrac(self):
    print(self.num,"/",self.den,end=" ",sep="")

  def __str__(self):
    if self.den!=1:
        return f"{self.num}/{self.den}"
    else:
        return f"{self.num}"
  def dec(self):
    return self.num/self.den
  def inFrac(self,frac_cad):
    if isinstance (frac_cad,str):
      if frac_cad.find("/")!=-1:
        self.num,self.den=frac_cad.split("/")
        self.num=int(self.num)
        self.den=int(self.den)
      else:
        self.num=int(frac_cad)
        self.den=1
      if self.den==0: #Validacion para den != 0
        self.den=1
        self.num=0
        return False
      else:
        return True
    else:
      return True

  def ingresarFrac(self):
    while(True):
      self.cadena=input("Ingresa el valor o Fraccion a/b: ")#Areglar entrada de decimales   ARREGLADO!!!
      try:
        if self.cadena.find("/")!=-1:
          self.num,self.den=self.cadena.split("/")
          self.num=int(self.num)
          self.den=int(self.den)

          if self.den==0:
            print("Denominador no puede ser 0")
            continue
          break
        else:
          self.num=int(self.cadena)
          self.den=1
        break
      except ValueError:
                print("Solo se permiten numeros enteros")
                continue

  def simplificar(self): #Ocultar metodo

    if(self.num<0 and self.den<0 or self.den<0):
      self.num=self.num*-1
      self.den=self.den*-1
    if(self.num==0):
      self.den=1
    if(abs(self.num)>abs(self.den)):
      i=2
      while(i<=abs(self.den)):
        if(self.num%i==0 and self.den%i==0):
          self.num=int(self.num/i)
          self.den=int(self.den/i)
        else:
          i+=1
        #print("i= ",i,self.num,"/",self.den)
    else:
      i=2
      while(i<=abs(self.num)):
        if(self.num%i==0 and self.den%i==0):
          self.num=int(self.num/i)
          self.den=int(self.den/i)
        else:
          i+=1
        #print(self.num,"/",self.den)

  def __mul__(self,other):
    if isinstance(other,Fraccion):
      numer=self.num*other.num
      denr=self.den*other.den
      result=Fraccion(numer,denr)
      result.simplificar()
      return result
    elif isinstance(other,int):
      result=Fraccion(self.num*other,self.den)
      result.simplificar()
      return result
    return NotImplemented

  def __add__(self,other):
    if isinstance(other,Fraccion):
      num_re=self.num*other.den+other.num*self.den
      den_re=self.den*other.den
      result=Fraccion(num_re,den_re)
      result.simplificar()
      return result
    return NotImplemented

  def __sub__(self,other):
    if isinstance(other,Fraccion):
      num_re=self.num*other.den-self.den*other.num
      den_re=self.den*other.den
      result=Fraccion(num_re,den_re)
      result.simplificar()
      return result
    return NotImplemented

  def __truediv__(self,other):     ##Crregir la division entre 0
    if isinstance(other,Fraccion):
      num_re=self.num*other.den
      den_re=self.den*other.num
      if den_re==0:
        return False
      result=Fraccion(num_re,den_re)
      result.simplificar()
      return result
    return NotImplemented

  def __lt__(self,other): #menor que
    if isinstance(other,Fraccion):
      return self.num*other.den<self.den*other.num
    elif isinstance(other,int):
      return self.num/self.den<other
    return NotImplemented

  def __le__(self,other):#Menor o igual que
    if isinstance(other,Fraccion):
      return self.num*other.den<=self.den*other.num
    elif isinstance(other,int):
      return self.num/self.den<=other
    return NotImplemented

  def __gt__(self,other):#Mayor que
    if isinstance(other,Fraccion):
      return self.num*other.den>self.den*other.num
    elif isinstance(other,int):
      return self.num/self.den>other
    return NotImplemented

  def __ge__(self,other):#mayor o igual que
    if isinstance(other,Fraccion):
      return self.num*other.den>=self.den*other.num
    elif isinstance(other,int):
      return self.num/self.den>=other
    return NotImplemented

  def __eq__(self,other):#igualdad
    if isinstance(other,Fraccion):
      return self.num*other.den==self.den*other.num
    elif isinstance(other,int):
      return self.num/self.den==other
    return NotImplemented

  def __ne__(self,other):#Desigualdad
    if isinstance(other,Fraccion):
      return self.num*other.den!=self.den*other.num
    elif isinstance(other,int):
      return self.num/self.den!=other
    return NotImplemented
  def __abs__(self):
    return Fraccion(abs(self.num),abs(self.den))

  def __pow__(self,other):
    if isinstance(other,int):
      num_re=self.num**other
      den_re=self.den**other
      result=Fraccion(num_re,den_re)
      result.simplificar()
      return result
    return NotImplemented
