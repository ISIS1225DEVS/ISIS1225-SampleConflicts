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
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    # TODO: Modificación de Est-1 en el Lab 2
    print("0- Salir")


def loadBooks():
    """
    Carga los libros
    """
    return controller.loadBooks('GoodReads/books-small.csv')


def loadTags():
    """
    Carga los Tags
    """
    return controller.loadTags('GoodReads/tags.csv')


def loadBookTags():
    """
    Cargar los Tags de libros
    """
    # TODO: Modificación de Est-1 en el Lab 2
    pass


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de libros....")
        books = loadBooks()
        print('Total de libros cargados: ' + str(lt.size(books)))

        # TODO: Modificación de Est-1 en el Lab 2


        # TODO: Modificación de Est-2 en el Lab 2
        print('Último libro cargado: ' + str(lt.lastElement(books)))

    elif int(inputs[0]) == 2:
        print("Cargando información de tags....")
        tags = loadTags()
        print('Total de tags cargados: ' + str(lt.size(tags)))
    elif int(inputs[0]) == 3:
        print("Cargando información de Book-Tags...")
        booktags = loadBookTags()
        print('Total de Book-Tags cargados: ' + str(lt.size(booktags)))

    else:
        sys.exit(0)
sys.exit(0)
