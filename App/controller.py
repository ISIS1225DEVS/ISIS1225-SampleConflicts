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
import model
import csv
import os


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.newCatalog()
    return control


# Funciones para la carga de datos

def loadBooks(control, filename):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    catalog = control["model"]
    booksfile = os.path.join(cf.data_dir, filename)
    catalog = model.addBooks(catalog, booksfile)
    return model.bookSize(catalog)


def loadTags(control, filename):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    catalog = control["model"]
    tagsfile = os.path.join(cf.data_dir, filename)
    input_file = csv.DictReader(open(tagsfile, encoding="utf-8"))
    catalog = model.createTagList(catalog)
    for tag in input_file:
        model.addTag(catalog, tag)
    return model.tagSize(catalog)


def loadBooksTags(catalog):
    btfile = cf.data_dir + filename
    return model.addBooksTags(btfile)
  

def loadBooksTags(control, filename):
    """
    Carga los tags de los libros del archivo
    """
    # TODO: Modificación de Est-1 y Est-2, Est-3 en el Lab 2
    pass


def firstBook(control):
    """
    Devuelve el primer libro del catalogo
    """
    # TODO: Modificación Est-3 en el Lab 2
    pass


def lastBook(control):
    """
    Devuelve el ultimo libro del catalogo
    """
    # TODO: Modificación Est-3 en el Lab 2
    pass

