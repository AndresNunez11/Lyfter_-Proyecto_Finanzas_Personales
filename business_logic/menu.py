from business_logic.financemanagerclass import finance_manager
from business_logic.categoryclass import Category
from business_logic.movementclass import Movement

#Opciones del menu, esta en el codigo pero podria trarse de un json o BD
#Utilizar la variable global en la mayuscula cuando es inmutable -- 
MENU_LIST= ["0- Salir",
"1- Agregar Categoria", "2- Agregar Movimiento", "3- Ver Categorias", 
"4- Ver movimientos", "5- Balance","6- Total Ingresos",
"7- Total de Gastos","8- Movimientos en Rango de Fechas"]

# Funcion principal para desplegar el menu
def menu(path_json_cat, path_json_mov, path_csv_report):
    try: 
        actions = finance_manager()
        #new_std_list = actions.read_json_file(path)
        while True:
            try:
                print(f"******Menu Principal******")
                print(f'Opciones:\n')
                for item in MENU_LIST:
                    print(f'{item}')
                option = int(input(f'Digite el número de la opción a elegir: \n'))
                print(f'La opción elegida es {MENU_LIST[option]}')
                match option:
                    case 0:
                        print(f'Fin de la aplicación')
                        break
                    case 1:
                        print(f'{MENU_LIST[1]}:\n')
                        category_text = input('Digite la nueva categria \n')
                        color_text = input('Digite el color \n')
                        new_category = Category(str(category_text),str(color_text))
                        print(new_category)
                        actions.add_category(new_category, path_json_cat)
                    case 2:
                        print(f'{MENU_LIST[2]}:\n')
                        movement_date= input('Ingrese la fecha:\n')
                        movement_description= input('Ingrese la descripcion:\n') 
                        movement_amount= input('Ingrese el monto de la transaccion:\n')
                        print(f'Categorias Disponibles')
                        print(f'{actions.list_category(path_json_cat)}')
                        filter_category=input('Ingrese la Categoria:\n')
                        movement_category=actions.filter_category(filter_category,path_json_cat)                     
                        movement_type = input('Ingreso o Gasto:\n')
                        new_movement = Movement(movement_date, movement_description, movement_amount, movement_category, movement_type)
                        print(new_movement)
                        actions.add_movement(new_movement,path_json_mov)                        
                    case 3:
                        print(f'{MENU_LIST[3]}:\n')
                        print(actions.list_category(path_json_cat))
                        
                    case 4: 
                        print(f'{MENU_LIST[4]}:\n')
                        print(actions.list_movement(path_json_mov))
                        
                    case 5:
                        print(f'{MENU_LIST[5]}:\n')
                        print(actions.Global_balance(path_json_mov))
                    case 6:
                        print(f'{MENU_LIST[6]}:\n')
                        print(actions.incoming_balance(path_json_mov))
                    case 7: 
                        print(f'{MENU_LIST[7]}:\n')
                        print(actions.expense_balance(path_json_mov))
                        
                    case 8:
                        print(f'{MENU_LIST[8]}:\n')
                        movements = actions.filter_movements_by_date_range("2026-07-15","2026-07-31",path_json_mov)
                        for movement in movements:
                            print(movement)
                        
                        
            except IndexError as error:
                print(f'La opción elegida no esta dentro de las disponibles. Error: {error}')
            except ValueError as e:
                print(f'El valor ingresado no es un numero entero {e}')
            except Exception as e:
                print(f'Error al desplegar el menu {e}')
    except Exception as e:
        print(f'Error al iniciar el menu, no lee archivo json. Error: {e}')
        