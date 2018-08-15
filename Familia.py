from Base import *

class Familia (object):
   idFamilia = None
   nombre = None
   lema = None
   enemigos = None

   def setFam (self, nom, lem):
       self.nombre = nom
       self.lema = lem

   def setFamilia(self):
       cursor=BD().run("Insert INTO Familia (idFamilia, Nombre, lema, Familia_idFamilia)values (null ,'" + self.nombre + "','" + self.lema + "',null);")
       self.idFamilia = cursor.lastrowid
       # "','" + self.enemigos

   def selectFamilia(self, idFamilia):
       BD().run("Select * from Familia Where idFamilia = " + idFamilia + ";")

   def updateFamilia(self):

       BD().run("update Familia set Nombre = '" + self.nombre + "', lema = '"+self.lema+"'  where idFamilia = '" + str(self.idFamilia) + "';")

   def deleteFamilia(self):

       BD().run("DELETE FROM Familia WHERE idFamilia = '%s'" % (self.idFamilia))

   @staticmethod
   def ListaFamilias():
        lista=[]
        bd = BD().run("SELECT * FROM Familia;")

        for item in bd:
            lista.append(item)

        return lista


   @staticmethod

   def unaFamilia(unIDFam):


        d = BD().run("Select * from Familia where idFamilia = '" + str(unIDFam) + "';")
        lista = d.fetchall()
        Family = Familia()

        Family.idFamilia = lista[0]["idFamilia"]
        Family.nombre = lista[0]["Nombre"]
        Family.lema = lista[0]["lema"]
        Family.enemigos = lista[0]["Familia_idFamilia"]

        return Family
