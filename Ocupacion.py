from Base import *

class Ocupacion (object):
   idOcupacion = None
   Tipo = None
   Familiares_Nombre = None

   def __init__(self, idOcupacion, Tipo, Familiares_Nombre):
       self.idOcupacion = idOcupacion
       self.Tipo = Tipo
       self.Familiares_Nombre = Familiares_Nombre

   def selectOcupacion (self, idOcupacion):

       BD().run("Select * from Ocupacion Where idOcupacion = " + idOcupacion + ";")
   #Cambiar insert por el otro
   def setOcupacion(self, idOcupacion, Tipo, Familiares_Nombre):
       BD().run("Insert into Ocupacion(idOcupacion ,Tipo, Familiares_Nombre) values (" + str(Tipo)+ "," + Familiares_Nombre)

   def updateOcupacion(self, Tipo, Familiares_Nombre):
       BD().run("Update Ocupacion Set Tipo = '"+Tipo+"', Familiares_Nombre = '"+Familiares_Nombre+"' Where Tipo = "+str(Tipo)+";")

   def deleteOcupacion(self, Tipo):

       BD().run("Delete from Ocupacion where Tipo = '" + str(Tipo) + "';")


   @staticmethod
   def ListaOcupacion():
       lista=[]
       bd = BD().run("SELECT * FROM Ocupacion")
       for item in bd:
           ocupa = Ocupacion()
           ocupa.idOcupacion =  item["idOcupacion"]
           ocupa.Tipo= item["Tipo"]
           ocupa.Familiares_Nombre = item["Familiares_Nombre"]
           lista.append(ocupa)
       return lista

