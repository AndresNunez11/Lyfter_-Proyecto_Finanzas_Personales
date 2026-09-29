import json
import os
from categoryclass import Category
from movementclass import Movement


HEATHERS_FILE = ["Fecha_Movimiento", "Descripcion", "Monto", "Categoria", "Tipo"]

# Leer archivo de Json con informacion de Movimientos, si no existe crea el archivo
def movement_read_json_file(path_json_file):
    movement_list = []
    try:
        with open(path_json_file, "r", encoding="utf-8" ) as file:
            data = json.load(file)
            for data_movement in data:
                movement_list.append(Movement(
                                data_movement["date"],
                                data_movement["description"],
                                data_movement["amount"],
                                data_movement["category"],
                                data_movement["type"]
                            ))
            return movement_list
    except FileNotFoundError:
        print(f"Archivo no encontrado, se creará uno nuevo {path_json_file}")
        return movement_list
    except json.JSONDecodeError:
        print("Archivo JSON corrupto, se inicia con lista vacía")
        return movement_list
    except Exception as e:
        print(f'Error al leer archivo JSON {e}')


# Funcion para salvar movimientos en archivo Json

def movement_save_json_file(movement_list, path_json_file):
    try:
        movements = [movement.to_dict() for movement in movement_list]
        with open(path_json_file, "w", encoding="utf-8" ) as file:
            json.dump(movements, file, indent=4, ensure_ascii=False)
        print('Movimeinto agregado')
    except Exception as e:
        print(f'Error al guardar los movimientos {e}')

