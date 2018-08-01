from Base import *

class Asentamiento (object):
    Nombre = None
    Ubicacion = None
    Familia_Nombre = None

    def __init__(self, Nombre, Ubicacion, Familia_Nombre):
        self.Nombre = Nombre
        self.Ubicacion = Ubicacion

    def selectAsentamiento (self,Nombre):

        BD().run("Select * from Asentamiento Where Nombre = " + str(Nombre) + ";")

    def setAsentamiento(self, Nombre, Ubicacion, Familia_Nombre):
        BD().run("Insert into Asentamiento(Nombre, Ubicacion, Familia_Nombre) values (" + str(Nombre) + "," + str(Ubicacion) + "," + str(Familia_Nombre))

    def updateAsentamiento(self, Nombre, Ubicacion, Familia_Nombre):
        BD().run("Update Asentamiento Set Nombre = '"+Nombre+"', Ubicacion = '"+Ubicacion+ "', Familia_Nombre = '"+Familia_Nombre+ "' Where Nombre = "+str(Nombre)+";")

    def deleteAsentamiento(self, Nombre):
        BD().run("Delete from Asentamiento where Nombre = '" + str(Nombre) + "';")