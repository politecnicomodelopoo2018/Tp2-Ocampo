from Base import *

class Familia (object):

    nombre = None
    lema = None
    enemigos = None

    def setNombre (self, nombre):
        self.nombre = nombre

    def setLema (self,lema):
        self.lema = lema

    def setEnemigos (self,enemigos):
        self.enemigos = enemigos

    def setFamilia(self):
        BD().run("INSERT INTO Familia (Nombre, lema, Familia_Enemigos) VALUES ('%s', '%s', '%s',)" % (self.Nombre, self.lema, self.Familia_Enemigos))

    def selectFamilia(self, lema):
        BD().run("Select * from Familia Where lema = " + str(lema) + ";")

    def updateFamilia(self, nombre, lema, enemigos):
        BD().run("Update Familia Set Nombre = '" + nombre + "', lema = '" + lema + "', Familia_Enemigos = '" + enemigos + "' Where Nombre = "+str(nombre)+";")

    def deleteFamilia(self, nombre):

        BD().run("Delete from Familia where Nombre = '" + str(nombre) + "';")