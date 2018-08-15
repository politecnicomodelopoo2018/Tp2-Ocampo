from Base import *

from Familia import *
from Familiares import Familiares
from Asentamiento import Asentamiento
from Ocupacion import Ocupacion

BD().SetConnection('127.0.0.1', 'root', 'alumno', 'mydb')

opcion = None
Fam = Familia()
Fams = Familiares()
Asen = Asentamiento()
Ocu = Ocupacion()

while opcion != 17:
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
   print("Ocupacion")
   print("13- Alta")
   print("14- Baja")
   print("15- Modificacion")
   print("16- ListaOcupaciones")
   print("17- Salir")
   opcion = int(input())


#Familia

   #Dar alta Familia
   if opcion == 1:
       name = input("Nombre familia")
       lema = input("lema")
       Fam.setFam(name, lema)
       Fam.setFamilia()#ver

   #Listar Familia
   elif opcion == 2:
       print(Familia.ListaFamilias())

   #Modificar Familia
   elif opcion == 3:

        print(Familia.ListaFamilias())

        updateAsen = int(input("Ingrese el id de la familia que desea modificar: "))

        Fam = Familia.unaFamilia(updateAsen)

        Fam.nombre = input("Escriba el nombre de la familia: ")

        Fam.lema = input("Escriba el lema de la familia: ")

        Fam.updateFamilia()



    #Dar baja Familia
   elif opcion == 4:

        print(Familia.ListaFamilias())

        deleteFam= int(input("Ingrese el id de la Familia que desea eliminar: "))

        Fam = Familia.unaFamilia(deleteFam)

        Fam.deleteFamilia()


#Familiares

        # Dar alta Familiares
   if opcion == 5:
       name = input("Nombre familiares")
       edad = input("edad")
       Fams.setFamilias(name, edad)
       Fams.setFamiliares()  # ver

       # Lista Familiares
   elif opcion == 6:
       print(Familiares.ListaFamiliares())

       # Modificar Familiares
   elif opcion == 7:

       print(Familiares.ListaFamiliares())

       updateFams = int(input("Ingrese el id del familiar que desea modificar: "))

       Fams = Familiares.unFamiliar(updateFams)

       Fams.Nombre = input("Escriba el nombre del familiar: ")

       Fams.Edad = input("Escriba el edad del familiar: ")

       Fams.updateFamiliares()



       # Dar baja Familiares
   elif opcion == 8:

       print(Familiares.ListaFamiliares())

       deletefams = int(input("Ingrese el id de la Familiar que desea eliminar: "))

       Fams = Familiares.unFamiliar(deletefams)

       Fams.deleteFamiliares()


#Asentamiento

    #Alta Asentamiento
   elif opcion == 9:

       name = input("Nombre Asentamiento")
       ubicacion = input("ubi")
       Asen.setAsen(name, ubicacion)
       Asen.setAsentamiento()  # ver

    #Baja Asentamiento
   elif opcion ==10:
       print(Asentamiento.ListaAsen())

       deleteAsen = int(input("Ingrese el id del Asentamiento que desea eliminar: "))

       Asenn = Asentamiento.unAsentamiento(deleteAsen)

       Asenn.deleteAsentamiento()

    #Modi Asentamiento
   elif opcion == 11:

       print(Asentamiento.ListaAsen())

       updateAsen = int(input("Ingrese el id del Asentamiento que desea modificar: "))

       Aseen = Asentamiento.unAsentamiento(updateAsen)

       Aseen.Nombre = input("Escriba el nombre del Asentamiento: ")

       Aseen.Ubicacion = input("Escriba la Ubicacion del Asentimento: ")

       Aseen.updateAsentamiento()


    #Lista Asentamiento
   elif opcion == 12:
       print(Asentamiento.ListaAsen())



#Ocupacion


    #Alta Ocupacion
   elif opcion == 13:

       tipo = input("Tipo de ocupacion")
       Ocu.setOcupacion(tipo)
       Ocu.setOcupa()  # ver


    #Baja Ocupacion
   elif opcion ==14:
       print(Ocu.ListaOcupacion())

       deleteOcu = int(input("Ingrese el id del Ocupacion que desea eliminar: "))

       Ocu = Ocu.unaOcupacion(deleteOcu)

       Ocu.deleteOcupacion()

    #Modi Asentamiento
   elif opcion == 15:

       print(Ocu.ListaOcupacion())

       updateOcu = int(input("Ingrese el id de la Ocupacion que desea modificar: "))

       Ocu = Ocu.unaOcupacion(updateOcu)

       Ocu.Tipo = input("Escriba el tipo de Ocupacion: ")

       Ocu.updateOcupacion()


    #Lista Asentamiento
   elif opcion == 16:
       print(Ocu.ListaOcupacion())
