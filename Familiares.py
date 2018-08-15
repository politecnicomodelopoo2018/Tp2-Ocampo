from Base import *

class Familiares (object):
   idFamiliar = None
   Nombre = None
   Edad = None
   Familia_Nombre = None

   def setFamilias (self, Nombre, Edad):
       self.Nombre = Nombre
       self.Edad = Edad

   def setFamiliares(self):
       cursor=BD().run("Insert INTO Familiares (idFamiliar, Nombre, Edad, Familia_idFamilia)values (null ,'" + self.Nombre + "','" + self.Edad + "',null);")
       self.idFamiliar = cursor.lastrowid

   def updateFamiliares(self):
       BD().run("update Familiares set Nombre = '" + self.Nombre + "', Edad = '"+self.Edad+"'  where idFamiliar = '" + str(self.idFamiliar) + "';")

   def deleteFamiliares(self):
       BD().run("DELETE FROM Familiares WHERE idFamiliar = '%s'" % (self.idFamiliar))

   @staticmethod
   def ListaFamiliares():
        lista=[]
        bd = BD().run("SELECT * FROM Familiares;")

        for item in bd:
            lista.append(item)

        return lista


   @staticmethod

   def unFamiliar(unIDFam):


        d = BD().run("Select * from Familiares where idFamiliar = '" + str(unIDFam) + "';")
        lista = d.fetchall()
        Family = Familiares()

        Family.idFamiliar = lista[0]["idFamiliar"]
        Family.Nombre = lista[0]["Nombre"]
        Family.Edad = lista[0]["Edad"]
        Family.Familia_Nombre = lista[0]["Familia_idFamilia"]

        return Family
