#!/usr/bin/python

# -*- coding: utf-8 -*-

import os


def menu():

    os.system('clear')

    print("Selecciona una opción")

    print("\t1 - Inserts")

    print("\t2 - Update")

    print("\t3 - Delete")

    print("\t4 - Selects")

    print("\t9 - salir")


while 1:

    # Mostramos el menu

    menu()

    # solicituamos una opción al usuario

    opcionMenu = input("inserta una opcion \n")

    if opcionMenu == "1":

        os.system('clear')

        input("Has pulsado la opcion de Inserts...\npulsa una tecla para continuar")

    elif opcionMenu == "2":

        os.system('clear')

        input("Has pulsado la opcion de Update...\npulsa una tecla para continuar")

    elif opcionMenu == "3":

        os.system('clear')

        input("Has pulsado la opcion de Delete...\npulsa una tecla para continuar")

    elif opcionMenu == "4":

        os.system('clear')

        input("Has pulsado la opcion de Selects...\npulsa una tecla para continuar")

    elif opcionMenu == "9":

        break

    else:

        os.system('clear')

        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")