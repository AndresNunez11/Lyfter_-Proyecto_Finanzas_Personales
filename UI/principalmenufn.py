import FreeSimpleGUI as sg
from UI.createmainwindowtype import create_main_window
from business_logic.financemanagerclass import FinanceManager
from business_logic.categoryclass import Category
from business_logic.movementclass import Movement
from datetime import datetime
from UI.movementtablefn import movement_table, movement_table_data
from UI.createcategorywindowtype import create_category_window
from UI.createaddcategorywindow import create_add_category_window
from UI.incomeexpenseselectwindow import create_select_expense_income_window
from UI.createaddmovementwindow import create_add_movement_window


def principal_menu_GUI(path_json_cat, path_json_mov, path_csv_report, theme):

    action = FinanceManager(path_json_cat, path_json_mov,path_csv_report)
    current_theme = theme
    main_window = create_main_window(current_theme,action) 
    windows = {
    "main": main_window
    }

    # Iniciamos el Event Loop
    while True:
        # El programa se "detiene" aquí (bloqueo) esperando una acción
        window, event, values = sg.read_all_windows()
        
        # Si el usuario cierra la ventana, rompemos el ciclo
        # ===============================================#
            # si cierras una ventana secundaria con la X, 
            # también la eliminas del diccionario. 
            # Si cierras la principal, sales del event loop
        #================================================#
        if event in (sg.WINDOW_CLOSED, "Salir"):
            if window == windows["main"]:
                break
            for key, open_window in list(windows.items()):
                if open_window == window:
                    open_window.close()
                    del windows[key]
                    break
            continue

        # Menú Inicio
        elif event == "Principal":
            window.close()
            del windows["main"]
            windows["main"] = create_main_window(
                    current_theme,
                    action
                    )            
        elif event == "Salir":
            break
        
        # Menú Administración
        # ----------------------------------------------Categorias----------------------------------------------------------#
        
        # Abrir Categorías
        #========================================================#
            # Se reemplza el esta validando por una variable, 
            # para validar por un diccionario, 
            # mejor practica para una estructura mas solida. 
        #========================================================#
        elif window == windows["main"] and event == "Categorías":
            if "categories" not in windows:
                windows["categories"] = create_category_window(current_theme,action)

        # Cerrar Categorías // Asegura que el evento corresponda a la ventana de Categorías
        #========================================================#
            # Se reemplza el esta validando por una variable, 
            # para validar por un diccionario, 
            # mejor practica para una estructura mas solida. 
        #========================================================#
        elif ("categories" in windows and window == windows["categories"] and event == "-CLOSE-CATEGORY-"):
            window.close()
            del windows["categories"]
        
        # Guardar categoría
        # ======================================================================================
        # Se crea una ventana con la cual se puedea agregar una nueva categoria
        # se debe validar que no esta vacia alguna d ela informacion
        # validar que ventana tiene el evento antes de cerrarla
        # ======================================================================================
        elif "categories" in windows and window == windows["categories"] and event == "-ADD-CATEGORY-":
            if "addcategory" not in windows:
                windows["addcategory"] = create_add_category_window(current_theme)
        
        elif ("addcategory" in windows and window == windows["addcategory"] and event == "-CLOSE-ADD-CATEGORY-"):
                window.close()
                del windows["addcategory"]

        elif "addcategory" in windows and window == windows["addcategory"] and event == "-PICK-ADD-CATEGORY-":
            try:
                name = values["-CATEGORY-NAME-"]
                color = values["-CATEGORY-COLOR-"]
                if not name.strip():
                    sg.popup_error("Debe ingresar un nombre de categoría")
                elif not color.strip():
                    sg.popup_error("Debe ingresar un color para la categoría")
                category = Category(name, color)
                action.add_category(category)
                sg.popup("Categoría agregada correctamente")
                windows["addcategory"].close()
                del windows["addcategory"]
                windows["categories"].close()
                del windows["categories"]
                windows["categories"] = create_category_window(
                    current_theme,
                    action
                )
            except Exception as e:
                sg.popup_error(str(e))
        
        #=====================================================================================================================#
        # -------------------------------------------------------Movimientos--------------------------------------------------#
        # ABRIR VENTANA PARA AGREGAR MOVIMIENTOS
        #=====================================================================================================================#
        elif window == windows["main"] and event == "Movimientos":
            if "select_movements" not in windows:
                windows["select_movements"] = create_select_expense_income_window(current_theme)
                # windows["movements"] = create_add_movement_window(current_theme,action)
                # window["-MOVEMENT-DATE-"].update(value = "")
        
        
        elif "select_movements" in windows and window == windows["select_movements"] and event == "-PICK-EXPENSE-":
                if "movements" not in windows:
                    windows["movements"] = create_add_movement_window(current_theme,action)
                    movememnt_type = "gasto"
                    print(movememnt_type)


        elif "select_movements" in windows and window == windows["select_movements"] and event == "-PICK-INCOME-":
                if "movements" not in windows:
                    windows["movements"] = create_add_movement_window(current_theme,action)
                    movememnt_type = "ingreso"
                    print(movememnt_type)
        
        elif "movements" in windows and window == windows["movements"] and event == "-PICK-MOVEMENT-DATE-":
                selected_date = sg.popup_get_date(
                title="Seleccionar fecha del movimiento",
                close_when_chosen=True
                )
                if selected_date:
                    month, day, year = selected_date
                    window["-MOVEMENT-DATE-"].update(
                    f"{day:02d}/{month:02d}/{year}"
                    )
        elif "movements" in windows and window == windows["movements"] and event == "-PICK-CATEGORY-MOVEMENT-":
                selected_name = values["-PICK-CATEGORY-MOVEMENT-"]
                selected_category = next(
                (
                    category
                    for category in action.categories
                    if category.name == selected_name
                ),
                None
                )
                if selected_category:
                    if not selected_category.name.strip():
                        sg.popup_error("Debe elegir una categoria para el movimiento")

        elif "movements" in windows and window == windows["movements"] and event == "-PICK-ADD-MOVEMENT-":
            try:
                movement_date = values["-MOVEMENT-DATE-"]
                movement_description = values["-DESCRIPTION-MOVEMENT-"]
                movement_amount = values["-AMOUNT-MOVEMENT-"]
                movement_category = selected_category
                if not movement_date.strip():
                    sg.popup_error("Debe ingresar la fecha del movimeinto")
                elif not movement_description.strip():
                    sg.popup_error("Debe ingresar una descripcion para el movimiento")
                elif not movement_amount.strip():
                    sg.popup_error("Debe ingresar un monto para el movimiento")
                elif not movement_category.name.strip():
                    sg.popup_error("Debe elegir una categoria para el movimiento")
                elif not movememnt_type.strip():
                    sg.popup_error("Debe elegir un tipo de movimiento")
                movement= Movement(movement_date,movement_description,movement_amount,movement_category,movememnt_type)
                action.add_movement(movement)
                sg.popup("Movimiento agregado correctamente")
                windows["movements"].close()
                del windows["movements"]
                windows["select_movements"].close()
                del windows["select_movements"]
                windows["main"].close()
                windows["main"] = create_main_window(
                                current_theme,
                                action
                            )            
            except Exception as e:
                sg.popup_error(str(e))

        elif ("select_movements" in windows and window == windows["select_movements"] and event == "-CLOSE-EXPENSE_INCOME-"):
                            window.close()
                            del windows["select_movements"]

        elif ("movements" in windows and window == windows["movements"] and event == "-CLOSE-MOVEMENT-"):
                    window.close()
                    del windows["movements"]
        #================================================================
        # --------------------------Reportes-------------------------#
        #================================================================

        elif window == windows["main"] and event == "Exportar Reporte a CSV":
            msj = action.export_movement_csv_file()
            sg.popup(f'Se exporta reporte a formato csv. Ruta {msj}')
        
        #================================================================
        # ------------Configuracion del tema-------------------------#
        #================================================================
        # Menú Configuración
        elif event == "Tema claro":
            current_theme = "LightBlue1"
            window.close()
            del windows["main"]
            windows["main"] = create_main_window(
                current_theme,
                action
            ) 

        elif event == "Tema oscuro":
            current_theme = "DarkGrey2"
            window.close()
            del windows["main"]
            windows["main"] = create_main_window(
            current_theme,
            action
            )

        # Menu para elegir si la tabla de movimientos se debe filtrar o no 
        elif event == "-ENABLE-FILTER-":
            
            enabled = values["-ENABLE-FILTER-"]
            
            # Mostrar u ocultar todos los controles de fecha
            filter_elements = [
                "-START-LABEL-",
                "-START-DATE-",
                "-PICK-START-",
                # "-START-CALENDAR-",
                "-END-LABEL-",
                "-END-DATE-",
                "-PICK-END-",
                # "-END-CALENDAR-",
                "-FILTER-DATES-"
            ]

            for key in filter_elements:
                window[key].update(visible=enabled)
                # print(hasattr(sg, "popup_get_date"))
            window.refresh()

            # Habilitar o deshabilitar los campos de fecha
            # window["-START-DATE-"].update(disabled=not enabled)
            # window["-END-DATE-"].update(disabled=not enabled)

            if not enabled:
                window["-START-DATE-"].update(value = "")
                window["-END-DATE-"].update(value = "")

                # Restaurar todos los movimientos
                table_values, row_colors = movement_table_data(
                    action.movements
                )

                window["-MOVEMENTS-TABLE-"].update(
                    values=table_values,
                    row_colors=row_colors
                )

        elif event == "-PICK-START-":
            selected_date = sg.popup_get_date(
                title="Seleccionar fecha inicial",
                close_when_chosen=True
            )

            if selected_date:
                month, day, year = selected_date
                window["-START-DATE-"].update(
                f"{day:02d}/{month:02d}/{year}"
                )
        elif event == "-PICK-END-":
            selected_date = sg.popup_get_date(
                title="Seleccionar fecha final",
                close_when_chosen=True
            )
            if selected_date:
                month, day, year = selected_date
                window["-END-DATE-"].update(
                    f"{day:02d}/{month:02d}/{year}"
                )

        elif event == "-FILTER-DATES-":
            try:
                start_date = datetime.strptime(
                    values["-START-DATE-"],
                    "%d/%m/%Y"
                ).date()

                end_date = datetime.strptime(
                    values["-END-DATE-"],
                    "%d/%m/%Y"
                ).date()

                if start_date > end_date:
                    sg.popup_error(
                        "La fecha inicial no puede ser posterior "
                        "a la fecha final."
                    )
                    continue

                # Filtrar los movimientos en memoria
                filtered_movements = [
                    movement
                    for movement in action.movements
                    if start_date <= movement.date <= end_date
                ]

                # Actualizar los datos y los colores de la tabla
                table_values, row_colors = movement_table_data(
                    filtered_movements
                )

                window["-MOVEMENTS-TABLE-"].update(
                    values=table_values,
                    row_colors=row_colors
                )

                if not filtered_movements:
                    sg.popup(
                        "No hay movimientos en el rango de fechas."
                    )

            except ValueError:
                sg.popup_error(
                    "Selecciona una fecha de inicio y una fecha final válidas."
                )
    # window.close()
    #====================================================================#
    # Esto garantiza que se cierren todas las ventanas registradas al salir
    #====================================================================#
    for open_window in list(windows.values()):
        open_window.close()

    windows.clear()