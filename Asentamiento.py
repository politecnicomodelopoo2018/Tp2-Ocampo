class Asentamiento (object):
    Nombre = None
    Ubicacion = None

    def __init__(self, Nombre, Ubicacion):
        self.Nombre = Nombre
        self.Ubicacion = Ubicacion

    def selectAsentamiento (self,Nombre):

        BD().run("Select * from Asentamiento Where Nombre = " + str(Nombre) + ";")

    def setAsentamiento(self, Nombre, Ubicacion):
        BD().run("Insert into Asentamiento(Nombre, Ubicacion) values (" + str(Nombre) + "'," + str(Ubicacion))

    def updateAsentamiento(self, Nombre, Ubicacion):
        BD().run("Update Familia Set Nombre = '" + Nombre + "', Ubicacion = " + str(Ubicacion) + ";")

    def deleteAsentamiento(self, Nombre):
        BD().run("Delete from Asentamiento where Nombre = '" + str(Nombre) + "';")