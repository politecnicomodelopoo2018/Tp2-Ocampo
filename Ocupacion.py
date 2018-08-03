from Base import *

class Ocupacion (object):

    Tipo = None
    Familiares_Nombre = None

    def __init__(self, Tipo, Familiares_Nombre):
        self.Tipo = Tipo
        self.Familiares_Nombre = Familiares_Nombre

    def selectOcupacion (self, Tipo):

        BD().run("Select * from Ocupacion Where Tipo = " + str(Tipo) + ";")

    def setOcupacion(self, Tipo, Familiares_Nombre):
        BD().run("Insert into Ocupacion(Tipo, Familiares_Nombre) values (" + str(Tipo)+ "," + Familiares_Nombre)

    def updateOcupacion(self, Tipo, Familiares_Nombre):
        BD().run("Update Ocupacion Set Tipo = '"+Tipo+"', Familiares_Nombre = '"+Familiares_Nombre+"' Where Tipo = "+str(Tipo)+";")

    def deleteOcupacion(self, Tipo):

        BD().run("Delete from Ocupacion where Tipo = '" + str(Tipo) + "';")