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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
assert cf

"""
En el modelo, se crean las estructuras de datos, es decir,
las variables donde se van a guardar los datos leidos de los
archivos CSV.

El modelo debe ser el unico sitio donde se modifican y manipulan
los datos.
"""


def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {"books": None,
               "tags": None,
               "book_tags": None}
    return catalog


# Funciones para agregar informacion al catalogo

def addBooks(catalog, booksfile):
    """
    Para guardar los libros provenientes del archivo CSV
    vamos a crear una lista, en donde quedarán todos los datos.

    No es importante entender como funciona esta lista por ahora.

    La funcion newList crea una lista de muchas formas. Una de ellas
    es leyendo todo lo que encuentre en el archivo indicado por filename.
    Cada linea del archivo quedará en una posicion de la lista.
    """
    catalog["books"] = lt.newList(datastructure="SINGLE_LINKED",
                                  filename=booksfile)
    return catalog


def addBookTags(catalog, booktagsfile):
    """
    Esta funcion guardar los booktags provenientes del archivo CSV.
    """
    # TODO: Modificaciones de Est-1 y Est-2, Est-3 en el Lab 2
    pass


def addTag(catalog, tag):
    """
    Para procesar el archivo de tags vamos a usar de otra forma la lista.
    En este caso, agregaremos cada linea del archivo a la lista, en lugar
    de usar la opcion de crearla con el nombre del archivo.
    """
    lt.addLast(catalog["tags"], tag)
    return catalog


def createTagList(catalog):
    """
    Esta funcion crea una lista vacia. Esta lista se utilizara
    para ir guardando la informacion en el archivo de tags.
    """
    catalog["tags"] = lt.newList(datastructure="SINGLE_LINKED")
    return catalog


def createBookTagList(catalog):
    """
    Esta funcion crea una lista vacia para booktags.
    """
    # TODO: Modificaciones de Est-1 y Est-2, Est-3 en el Lab 2
    pass


def addBookTag(catalog, booktag):
    """
    Esta funcion agrega un elemento a lista de booktags.
    """
    # TODO: Modificaciones de Est-1 y Est-2, Est-3 en el Lab 2
    pass


# Funciones de consulta

def bookSize(catalog):
    # TODO Modificaciones de Est-3 en el Lab 2
    pass


def tagSize(catalog):
    # TODO Modificaciones de Est-3 en el Lab 2
    pass


def bookTagSize(catalog):
    # TODO Modificaciones de Est-3 en el Lab 2
    pass


def firstBook(catalog):
    # TODO Modificaciones de Est-3 en el Lab 2
    pass

def addBookTags():
    bts = lt.newList(datastructure='SINGLE_LINKED',
    filename=booktagsfile)
    return bts
=======
def lastBook(catalog):
    # TODO Modificaciones de Est-3 en el Lab 2
    pass

