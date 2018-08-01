class Familiares (object):

    Nombre = None
    Edad = None

    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad = Edad

    def selectFamiliares (self, Nombre):

        BD().run("Select * from Familiares Where lema = " + str(Nombre) + ";")

    def setFamiliares(self, Nombre, Edad):
        BD().run("Insert into Familiares(Nombre, Edad) values (" + str(Nombre) + "'," + Edad + ",")

    def updateFamiliares(self, Nombre, Edad):
        BD().run("Update Familiares Set Nombre = '" + Nombre + "', Edad = " + Edad + ";")

    def deleteFamiliares(self, Nombre):
        BD().run("Delete from Familia where Nombre = '" + str(Nombre) + "';")
