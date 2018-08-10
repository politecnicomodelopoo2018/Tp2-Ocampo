from Base import *

class Familiares (object):

    Nombre = None
    Edad = None
    Familia_Nombre = None


    def setNombre (self, Nombre):
        self.Nombre = Nombre

    def setEdad(self, Edad):
        self.Edad = Edad

    def setFamiliaNombre (self, Familia_Nombre):
        self.Familia_Nombre = Familia_Nombre

    def selectFamiliares (self, Nombre):

        BD().run("Select * from Familiares Where Nombre = " + str(Nombre) + ";")

    def setFamiliares(self, Nombre, Edad, Familia_Nombre):
        BD().run("Insert into Familiares(Nombre, Edad, Familia_Nombre) values (" + str(Nombre) + "," + Edad + "," + str(Familia_Nombre))

    def updateFamiliares(self, Nombre, Edad, Familia_Nombre):
        BD().run("Update Familiares Set Nombre = '" + Nombre + "', Edad = '" + Edad + "', Familia_Nombre = '" + Familia_Nombre + "' Where Nombre = "+str(Nombre)+";")

    def deleteFamiliares(self, Nombre):
        BD().run("Delete from Familia where Nombre = '" + str(Nombre) + "';")
