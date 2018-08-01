class Familia (object):

    nombre = None
    lema = None
    enemigos = None

    def __init__(self, nombre, lema, enemigos):
        self.nombre = nombre
        self.lema = lema
        self.enemigos = enemigos

    def selectFamilia (self,lema):

        BD().run("Select * from familia Where lema = " + str(lema) + ";")

    def setFamilia(self, nombre, lema, enemigos):
        BD().run("Insert into Copa(Nombre, lema, familia_enemigos) values (" + str(nombre) + "'," + str(lema) + "," + str(enemigos))

    def updateFamilia(self, nombre, lema, enemigos):
        BD().run("Update Familia Set Nombre = '" + nombre + "', lema = " + str(lema) + " where Familia_Enemgios = " + str(enemigos) + ";")

    def deleteFamilia(self, nombre):

        BD().run("Delete from Familia where Nombre = '" + str(nombre) + "';")