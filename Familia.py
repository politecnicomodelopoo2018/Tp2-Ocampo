class Familia (object):
    nombre = None
    lema = None
    enemigos = None

    def __init__(self, nombre, lema, enemigos):
        self.nombre = nombre
        self.lema = lema
        self.enemigos = enemigos


    def selectFamilia (self,nombre, lema, enemigos):
