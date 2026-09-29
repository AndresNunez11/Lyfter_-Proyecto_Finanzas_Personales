import json
import os
from categoryclass import Category

HEATHERS_FILE = ["Categoria", "Color"]

# Leer archivo de Json con informacion de Movimientos, si no existe crea el archivo
def category_read_json_file(path_json_file):
    category_list = []
    try:
        with open(path_json_file, "r", encoding="utf-8" ) as file:
            data = json.load(file)
            for data_category in data:
                category_list.append(Category(
                    data_category["name"],
                    data_category["color"]
                ))
            return category_list
    except FileNotFoundError:
        print(f"Archivo no encontrado, se creará uno nuevo {path_json_file}")
        return category_list
    except json.JSONDecodeError:
        print("Archivo JSON corrupto, se inicia con lista vacía")
        return category_list
    except Exception as e:
        print(f'Error al leer archivo JSON {e}')

# Guardar datos en json -- simula BD
#  Metodo dump
# Convierte estructuras de Python como:
# diccionarios (dict)
# listas (list)
# strings, números, booleanos
# en formato JSON
# y los escribe en un archivo 


def category_save_json_file(category_list, path_json_file):
    try:
        categories = [category.to_dict() for category in category_list]
        with open(path_json_file, "w", encoding="utf-8" ) as file:
            json.dump(categories, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Error al guardar las categorias {e}')