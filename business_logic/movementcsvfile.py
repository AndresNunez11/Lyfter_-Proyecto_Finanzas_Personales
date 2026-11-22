import csv
import os
from business_logic.categoryclass import Category
from business_logic.movementclass import Movement

HEADERS_FILE = ["Fecha_Movimiento", "Descripcion", "Monto", "Categoria","Color_Categoria", "Tipo"]


# Leer archivo de CSV con informacion de Movimientos, si no existe crea el archivo
# def movement_read_csv_file(path_csv_file):
#     try:
#         movement_list = []
#         if(os.path.exists(path_csv_file)):
#             with open(path_csv_file,'r', newline="", encoding='utf-8')as file:
#                 reader = list(csv.DictReader(file))
#                 if not (reader): #No utilizar any para evitar consumir el primer dato --if not any--
#                     print("El CSV está vacío (sin datos)")
#                 else:
#                     for i, row in enumerate(reader):
#                         # print(f'Linea #{i}')
#                         # print(f"Estudiante: {row}")
#                         movement_list.append(row)
#             # print(f'Archivo csv leido correctamente')
#         else:
#             print('El archivo no ha sido exportado anteriormente')
#         return movement_list
#     except Exception as e:
#         print(f'Error al leer archivo {e}')

    


def movement_save_csv_file(movement_list, path_csv_file):
    try:
        myheaders = HEADERS_FILE
        movements = [movement.to_csv_dict() for movement in movement_list]
        with open(path_csv_file, "w", newline="", encoding="utf-8" ) as file:
            writer= csv.DictWriter(file, myheaders)
            writer.writeheader()
            writer.writerows(movements)
        msj =  f'{path_csv_file}'
        return msj  # print('Movimeinto agregado')
        # print('Movimeinto agregado')
    except Exception as e:
        print(f'Error al guardar los movimientos {e}')