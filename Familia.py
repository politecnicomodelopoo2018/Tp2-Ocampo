from Base import *

class Familia (object):

    nombre = None
    lema = None
    enemigos = None

    def __init__(self, nombre, lema, enemigos):
        self.nombre = nombre
        self.lema = lema
        self.enemigos = enemigos

    def selectFamilia (self,lema):

        BD().run("Select * from Familia Where lema = " + str(lema) + ";")

    def setFamilia(self, nombre, lema, enemigos):
        BD().run("Insert into Copa(Nombre, lema, Familia_Enemigos) values (" + str(nombre) + "," + str(lema) + "," + str(enemigos))

    def updateFamilia(self, nombre, lema, enemigos):
        BD().run("Update Familia Set Nombre = '" + nombre + "', lema = '" + lema + "', Familia_Enemigos = '" + enemigos + "' Where Nombre = "+str(nombre)+";")

    def deleteFamilia(self, nombre):

        BD().run("Delete from Familia where Nombre = '" + str(nombre) + "';")