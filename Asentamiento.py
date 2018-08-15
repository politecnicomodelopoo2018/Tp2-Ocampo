from Base import *

class Asentamiento (object):
   idAsentamiento = None
   Nombre = None
   Ubicacion = None
   Familia_Nombre = None

   def setAsen (self, Nom, Ubi):
       self.Nombre = Nom
       self.Ubicacion = Ubi

   def selectAsentamiento (self,idAsentamiento):
       BD().run("Select * from Asentamiento Where idAsentamiento = " + idAsentamiento + ";")

   def setAsentamiento(self):
       cursor = BD().run( "Insert INTO Asentamiento(idAsentamiento, Nombre, Ubicacion, Familia_idFamilia)values (null ,'" + self.Nombre + "','" + self.Ubicacion + "',null);")
       self.idFamilia = cursor.lastrowid

   def updateAsentamiento(self):
       BD().run("update Asentamiento set Nombre = '" + self.Nombre + "', Ubicacion = '"+self.Ubicacion+"'  where idAsentamiento = '" + str(self.idAsentamiento) + "';")

   def deleteAsentamiento(self):
       BD().run("DELETE FROM Asentamiento WHERE idAsentamiento = '%s'" % (self.idAsentamiento))


   @staticmethod
   def ListaAsen():
        lista=[]
        bd = BD().run("SELECT * FROM Asentamiento;")

        for item in bd:
            lista.append(item)

        return lista


   @staticmethod

   def unAsentamiento(IdAsen):


        d = BD().run("Select * from Asentamiento where idAsentamiento = '" + str(IdAsen) + "';")
        lista = d.fetchall()
        Asent = Asentamiento()

        Asent.idAsentamiento = lista[0]["idAsentamiento"]
        Asent.Nombre = lista[0]["Nombre"]
        Asent.Ubicacion = lista[0]["Ubicacion"]
        Asent.Familia_Nombre = lista[0]["Familia_idFamilia"]

        return Asent

