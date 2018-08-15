from Base import *

class Asentamiento (object):
   idAsentamiento = None
   Nombre = None
   Ubicacion = None
   Familia_Nombre = None

   def setAsen (self, idAsentamiento, Nombre, Ubicacion, Familia_Nombre):
       self.idAsentamiento = idAsentamiento
       self.Nombre = Nombre
       self.Ubicacion = Ubicacion
       self.Familia_Nombre = Familia_Nombre

   def selectAsentamiento (self,idAsentamiento):

       BD().run("Select * from Asentamiento Where idAsentamiento = " + idAsentamiento + ";")

   def setAsentamiento(self, idAsentamiento, Nombre, Ubicacion, Familia_Nombre):
       self.setAsen(idAsentamiento, Nombre, Ubicacion, Familia_Nombre)
       BD().run("INSERT INTO Asentamiento Values ( '%s','%s', '%s', '%s')" % (self.idAsentamiento, self.Nombre, self.Ubicacion, self.Familia_Nombre))

   def updateAsentamiento(self):
       BD().run("UPDATE Asentamiento SET idAsentamiento = '%s', Nombre = '%s',  Ubicacion = '%s', Familia_Nombre = '%s'" "Where Nombre = %s" % (self.idAsentamiento, self.Nombre, self.Ubicacion, self.Familia_Nombre))

   def deleteAsentamiento(self):
       BD().run("DELETE FROM Asentamiento WHERE idAsentamiento= '%s'" % (self.idAsentamiento))



   @staticmethod
   def ListaAsentamiento():
       lista=[]
       bd = BD().run("SELECT * FROM Asentamiento")
       for item in bd:
           casa = Asentamiento()
           casa.idAsentamiento = item["idAsentamiento"]
           casa.Nombre= item["Nombre"]
           casa.Ubicacion = item["Ubicacion"]
           casa.Familia_Nombre = item["Familia_Nombre"]
           lista.append(casa)
       return lista


