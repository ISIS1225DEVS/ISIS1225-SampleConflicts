"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import sys
import controller
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    # TODO: Mods de Est-1 en el Lab 2, agregar opcion 3
    print("3- Cargar Booktags")
    print("0- Salir")


def loadBooks(control):
    """
    Carga los libros
    """
    books = controller.loadBooks(control,
                                 "GoodReads/books-small.csv")
    return books


def loadTags(control):
    """
    Carga los Tags
    """
    tags = controller.loadTags(control,
                               "GoodReads/tags.csv")
    return tags


def loadBooksTags(control):
    """
    Cargar los Tags de libros
    """
    # TODO: Mods de Est-1 en el Lab 2
    pass


def firstBook(control):
    """
    Devuelve el primer libro del catalogo
    """
    # TODO: Mods de Est-1 en el Lab 2
    pass


def lastBook(control):
    # TODO: Mods de Est-2 en el Lab 2
    """
    Devuelve el último libro cargado
    """
    last = controller.lastBook(control)
    return last


# Se crea el controlador asociado a la vista
control = newController()

# main del ejercicio
if __name__ == "__main__":

    """
    Menu principal
    """
    working = True
    # ciclo del menu
    while working:
        printMenu()
        inputs = input("Seleccione una opción para continuar\n")
        if int(inputs[0]) == 1:
            print("Cargando información de libros....")
            books = loadBooks(control)
            print("Total de libros cargados: " + str(books) + "\n")

            # TODO: Mods de Est-1 en el Lab 2
            first = None

            # TODO: Mods de Est-2 en el Lab 2
            last = lastBook(control)
            print("Último libro cargado:\n" + str(last) + "\n")

        elif int(inputs[0]) == 2:
            print("Cargando información de tags....")
            tags = loadTags(control)
            print("Total de tags cargados: " + str(tags) + "\n")

        elif int(inputs[0]) == 3:
            # TODO: Mods de Est-3 en el Lab 2
            pass

        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            print("Opcion erronea, vuelva a elegir.\n")
    sys.exit(0)
