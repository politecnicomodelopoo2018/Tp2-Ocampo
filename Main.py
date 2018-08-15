from Base import *

from Familia import *
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
   print("4- ListaDeFamilia")
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

   #Dar alta Familia
   if opcion == 1:
       name = input("Nombre familia")
       lema = input("lema")
       Fam.setFam(name, lema)
       Fam.setFamilia()#ver

   #Dar baja Familia
   elif opcion == 2:
       print('hola')


   #Modificar Familia
   elif opcion == 3:

        print(Familia.ListaFamilias())

        updateFamily = int(input("Ingrese el id de la familia que desea modificar: "))

        Fam = Familia.unaFamilia(updateFamily)

        Fam.nombre = input("Escriba el nombre de la familia: ")

        Fam.lema = input("Escriba el lema de la familia: ")

        Fam.updateFamilia()

        print(Fam.nombre, Fam.lema, Fam.idFamilia)


   elif opcion == 4:

        print(Familia.ListaFamilias())

        deleteFamily = int(input("Ingrese el id de la Familia que desea eliminar: "))

        Family = Familia.unaFamilia(deleteFamily)

        Family.deleteFamilia()




