from abc import ABCMeta , abstractmethod
import random

class salarie (metaclass = ABCMeta) :
    _count = 0
    def __init__(self,nom,num,ec,adr,salaire):
        self.__nom = nom
        self.__num = num
        self.__ec = ec
        self.__adr = adr
        self.__salaire = salaire
        salarie._count += 1

    #getters
    
    @property
    def getnom (self) :
            return self.__nom
    @property
    def getnum(self) :
            return self.__num
    @property
    def getec (self) :
            return self.__ec
    @property
    def getadr (self) :
            return self.__adr
    @property
    def getsalaire (self) :
            return self.__salaire
    @property
    def getcount (self) :
           return self._count
    
#setter
    def setnom (self,nom):
           self.__nom = nom
    def setnum (self,num):
           self.__num = num
    def setec (self,ec):
           self.__ec = ec
    def setadr (self,adr):
           self.__adr = adr
    def setsalaire (self,salaire):
           self.__salaire = salaire

#methode
    def matricule (self):      
           matricule = (random.randint(1,100))
           return matricule
    def __str__(self) :
           print(f"Matricule ={self.matricule()} \n Name = {self.getnom} \n Number = {self.getnum} \n Civil state = {self.getec} \n Adress = {self.getadr} \n Base salary = {self.getsalaire}DH")

    @abstractmethod
    def __eq__(self):
           pass
    
    @abstractmethod
    def salaire(self):
           pass
    

class patron (salarie):
       def __init__(self,nom,num,ec,adr,salaire,P):
              super().__init__(nom,num,ec,adr,salaire)
              self.__P = P

       @property
       def getP (self):
              return self.__P
       
       def setP (self,P):
              self.__P = P

       
       def matricule(self):
              return super().matricule()
        
       def salaire (self):
              return (self.getsalaire + self.getP)

       def __str__(self):
               print(f"Risk premium :{self.getP}DH \n Total Salary ={self.salaire()}DH")
               return super().__str__() 


       def __eq__(self,P2):
              P1 = self.matricule(),self.salaire()
              P2 = self.matricule(),self.salaire()
              if (P1 == P2) :
                     return True
              else :
                     return False
              
   
class vendeur (salarie):
       def __init__(self,nom,num,ec,adr,salaire,COM,SV):
              super().__init__(nom,num,ec,adr,salaire)
              self.__COM = COM
              self.__SV =SV

       def getCOM (self):
              return self.__COM
       def getSV (self):
              return self.__SV
       
       def setCOM (self,COM):
              self.__COM = COM

       def setSV (self,SV):
              self.__SV = SV

       def salaire (self):
              return (self.getsalaire + self.getCOM)

       def __str__(self):
               print(f"Upper hierarchy ={self.GetSV} \n Total Salary = {self.salaire()}DH")
               return super().__str__()
       
       def __eq__(self,P2):
            P1 = self.matricule(),self.salaire()
            P2 = self.matricule(),self.salaire()
            if (P1 == P2) :
                    return True
            else :
                    return False 
            

class caissières (salarie):
       def __init__(self,nom,num,ec,adr,salaire,SV):
              super().__init__(nom,num,ec,adr,salaire)
              self.__SV =SV


       def getSV (self):
              return self.__SV
       def setSV (self,SV):
              self.__SV = SV
        
       def __str__(self):
              print(f"Upper hierarchy ={self.getSV}")
              return super().__str__()
       
      
       def __eq__(self,P2):
            P1 = self.matricule(),self.getsalaire()
            P2 = P2.matricule(),P2.getsalaire()
            if (P1 == P2) :
                    return True
            else :
                    return False 
            

w =patron ("wissal",34,"cele","marrakech",100000,30)
m =patron ("meryam",20,"cele","marrakech",10000000,5000)
print(w.__eq__(m))