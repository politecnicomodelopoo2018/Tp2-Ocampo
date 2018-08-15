from Base import *

from Familia import *
from Familiares import Familiares
from Asentamiento import Asentamiento

BD().SetConnection('127.0.0.1', 'root', 'alumno', 'mydb')

opcion = None
Fam = Familia()
Fams = Familiares()
Asen = Asentamiento()


while opcion != 13:
   print("Familia")
   print("1- Alta")
   print("2- ListaDeFamilia ")
   print("3- Modificacion")
   print("4- Baja")
   print("Familiares")
   print("5- Alta")
   print("6- ListarFamiliares")
   print("7- Modificacion")
   print("8- Baja")
   print("Asentamiento")
   print("9- Alta")
   print("10- Baja")
   print("11- Modificacion")
   print("12- ListaAsentamientos")
   print("13- Salir")
   opcion = int(input())

   #Dar alta Familia
   if opcion == 1:
       name = input("Nombre familia")
       lema = input("lema")
       Fam.setFam(name, lema)
       Fam.setFamilia()#ver

   #Dar listar Familia
   elif opcion == 2:
       print(Familia.ListaFamilias())

   #Modificar Familia
   elif opcion == 3:

        print(Familia.ListaFamilias())

        updateFamiliares = int(input("Ingrese el id de la familia que desea modificar: "))

        Fam = Familia.unaFamilia(updateFamiliares)

        Fam.nombre = input("Escriba el nombre de la familia: ")

        Fam.lema = input("Escriba el lema de la familia: ")

        Fam.updateFamilia()



    #Dar baja Familia
   elif opcion == 4:

        print(Familia.ListaFamilias())

        deleteAse = int(input("Ingrese el id de la Familia que desea eliminar: "))

        Asenn = Familia.unaFamilia(deleteAse)

        Asenn.deleteFamilia()

        # Dar alta Familiares
   if opcion == 5:
       name = input("Nombre familiares")
       edad = input("edad")
       Fams.setFamilias(name, edad)
       Fams.setFamiliares()  # ver

       # Dar listar Familiares
   elif opcion == 6:
       print(Familia.ListaFamiliares())

       # Modificar Familiares
   elif opcion == 7:

       print(Familiares.ListaFamiliares())

       updateFamiliares = int(input("Ingrese el id del familiar que desea modificar: "))

       Familiar = Familiares.unFamiliar(updateFamiliares)

       Familiar.Nombre = input("Escriba el nombre del familiar: ")

       Familiar.Edad = input("Escriba el edad del familiar: ")

       Familiar.updateFamiliares()



       # Dar baja Familiares
   elif opcion == 8:

       print(Familiares.ListaFamiliares())

       deleteAse = int(input("Ingrese el id de la Familiar que desea eliminar: "))

       Asenn = Familiares.unFamiliar(deleteAse)

       Asenn.deleteFamiliares()



   elif opcion == 9:

       name = input("Nombre Asentamiento")
       ubicacion = input("ubi")
       Fams.setFamilias(name, ubicacion)
       Fams.setFamiliares()  # ver

   elif opcion ==10:
       print(Asentamiento.ListaAsen())

       deleteAse = int(input("Ingrese el id del Asentamiento que desea eliminar: "))

       Asenn = Asentamiento.unAsentamiento(deleteAse)

       Asenn.deleteAsentamiento()

   elif opcion == 11:


   elif opcion == 12:
       print(Asentamiento.ListaAsen())
