from Base import *

class Ocupacion (object):
   idOcupacion = None
   Tipo = None
   Familiares_Nombre = None

   def setOcupacion(self, Tipo):
       self.Tipo = Tipo

   def selectOcupacion (self, idOcupacion):

       BD().run("Select * from Ocupacion Where idOcupacion = " + idOcupacion + ";")

   #Cambiar insert por el otro

   def setOcupa(self):
       cursor=BD().run("Insert INTO Ocupacion (idOcupacion, Tipo, Familiares_idFamiliar)values (null ,'" + self.Tipo + "',null);")
       self.idFamilia = cursor.lastrowid

   def updateOcupacion(self):
       BD().run("update Ocupacion set Tipo = '" + self.Tipo + "'  where idOcupacion = '" + str(self.idOcupacion) + "';")

   def deleteOcupacion(self):
       BD().run("DELETE FROM Ocupacion WHERE idOcupacion = '%s'" % (self.idOcupacion))


   @staticmethod
   def ListaOcupacion():
        lista=[]
        bd = BD().run("SELECT * FROM Ocupacion;")

        for item in bd:
            lista.append(item)

        return lista


   @staticmethod

   def unaOcupacion(unIDOcu):


        d = BD().run("Select * from Ocupacion where idOcupacion = '" + str(unIDOcu) + "';")
        lista = d.fetchall()
        ocu = Ocupacion()

        ocu.idOcupacion = lista[0]["idOcupacion"]
        ocu.Tipo = lista[0]["Tipo"]
       # ocu.Familiares_Nombre = lista [0]["Familiares_idFamiliar"]
        return ocu
