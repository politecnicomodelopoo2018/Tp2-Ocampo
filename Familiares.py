from Base import *

class Familiares (object):
   idFamiliar = None
   Nombre = None
   Edad = None
   Familia_Nombre = None

   def setFamilias (self, idFamiliar, Nombre, Edad, Familia_Nombre):
       self.idFamiliar = idFamiliar
       self.Nombre = Nombre
       self.Edad = Edad
       self.Familia_Nombre = Familia_Nombre
#Ver de poner self.idFamiliar
   def selectFamiliares (self):

       BD().run("Insert INTO Familia values (Null ,'" + self.Nombre + "','" + self.Edad + "'," + "Null" + ")")

   def setFamiliares(self, idFamiliar, Nombre, Edad, Familia_Nombre):
       self.setFamilias(idFamiliar ,Nombre,Edad, Familia_Nombre)
       BD().run("INSERT INTO Familiares Values ('%s', '%s', '%s', '%s')" % (self.idFamiliar, self.Nombre, self.Edad, self.Familia_Nombre))


   def updateFamiliares(self):
       BD().run("UPDATE Familiares SET idFamiliar = '%s', Nombre = '%s',  Edad = '%s', Familia_Nombre = '%s'" "Where Nombre = %s" % (self.idFamiliar, self.Nombre, self.Edad, self.Familia_Nombre))


   def deleteFamiliares(self):
       BD().run("DELETE FROM Familiares WHERE idFamiliar = '%s'" % (self.idFamiliar))

   @staticmethod
   def ListaFamiliares():
       lista=[]
       bd = BD().run("SELECT * FROM Familiares")
       for item in bd:
           familiar = Familiares()
           familiar.idFamiliar = item["idFamiliar"]
           familiar.Nombre= item["Nombre"]
           familiar.Edad = item["Edad"]
           familiar.Familia_Nombre = item["Familia_Nombre"]
           lista.append(familiar)
       return lista

