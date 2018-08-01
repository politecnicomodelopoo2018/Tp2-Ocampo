class Ocupacion (object):
    Tipo = None

    def __init__(self, Tipo):
        self.Tipo = Tipo

    def selectOcupacion (self, Tipo):

        BD().run("Select * from Ocupacion Where Tipo = " + str(Tipo) + ";")

    def setOcupacion(self, Tipo):
        BD().run("Insert into Ocupacion(Tipo) values (" + str(Tipo))

    def updateOcupacion(self, Tipo):
        BD().run("Update Ocupacion Set Tipo = '" + Tipo + " where Tipo = " + str(Tipo) + ";")

    def deleteOcupacion(self, Tipo):

        BD().run("Delete from Ocupacion where Tipo = '" + str(Tipo) + "';")