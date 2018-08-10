from Base import *

from Familia import Familia
from Familiares import Familiares
from Asentamiento import Asentamiento

BD().SetConnection('127.0.0.1', 'root', 'alumno', 'mydb')

opcion = None
Fam = Familia()
Fams = Familiares()
Asen = Asentamiento()


while opcion != 11:
    print("Familia")
    print("1- Alta")
    print("2- Baja ")
    print("3- Modificacion")
    print("4- ListaDeReinos")
    print("Familiares")
    print("5- Alta")
    print("6- Baja")
    print("7- Modificacion")
    print("Asentamiento")
    print("8- Alta")
    print("9- Baja")
    print("10- Modificacion")
    print("11- Salir")
    opcion = int(input())

    if opcion == 1:
        print("Nombre familia")
        name = input()
        Fam.setNombre(name)
        print("lema")
        lema = input()
        Fam.setLema(lema)
        print("enemigos")
        enemigos = input()
        Fam.setEnemigos(enemigos)
        Fam.setFamilia(name, lema, enemigos)



