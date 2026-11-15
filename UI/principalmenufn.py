import FreeSimpleGUI as sg
from UI.createmainwindowtype import create_main_window
from business_logic.financemanagerclass import finance_manager
from business_logic.categoryclass import Category
from datetime import datetime
from UI.movementtablefn import movement_table, movement_table_data
from UI.createcategorywindowtype import create_category_window
from UI.createaddcategorywindow import create_add_category_window


def principal_menu_GUI(path_json_cat, path_json_mov, path_csv_report, theme):

    action = finance_manager(path_json_cat, path_json_mov,path_csv_report)
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
            print("Mostrar pantalla principal")
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

        # elif window == main_window and event =="Categorías":
        #     if categories_window is None:
        #         categories_window = create_category_window(current_theme,action)
        #         windows.append(categories_window)
        
        # Cerrar Categorías // Asegura que el evento corresponda a la ventana de Categorías
        #========================================================#
            # Se reemplza el esta validando por una variable, 
            # para validar por un diccionario, 
            # mejor practica para una estructura mas solida. 
        #========================================================#
        elif ("categories" in windows and window == windows["categories"] and event == "-CLOSE-CATEGORY-"):
            window.close()
            del windows["categories"]
        
        # elif event == "-CLOSE-CATEGORY-":
        #     window.close()
        #     categories_window = None
        #     if window in windows:
        #         windows.remove(window)
        
        
        # Guardar categoría
        #========================================================#
        # Se crea una ventana con la cual se puedea agregar una nueva categoria
        # se debe validar que no esta vacia alguna d ela informacion
        # validar que ventana tiene el evento antes de cerrarla
        #========================================================#
        elif window == windows["categories"] and event == "Ingresar Categoria":
            if "addcategory" not in windows:
                windows["addcategory"] = create_add_category_window(current_theme)
        
        elif ("addcategory" in windows and window == windows["addcategory"] and event == "-CLOSE-ADD-CATEGORY-"):
                window.close()
                del windows["addcategory"]

        elif window == windows["addcategory"] and event == "-PICK-ADD-CATEGORY-":
            try:
                name = values["-CATEGORY-NAME-"]
                color = values["-CATEGORY-COLOR-"]
                if not name.strip():
                    sg.popup_error("Debe ingresar un nombre de categoría")
                elif not color.strip():
                    sg.popup_error("Debe ingresar un color para la categoría")
                # print("Nombre:", name)
                # print("Color:", color)
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




        # elif event == "-SAVE-CATEGORY-":
        #     name = values["-CATEGORY-NAME-"]
        #     color = values["-CATEGORY-COLOR-"]
        #     print("Nombre:", name)
        #     print("Color:", color)

        # -------------------------------------------------------MOvimientos--------------------------------------------------#
        elif event == "Movimientos":
            print("Abrir gestión de movimientos")

        # ------------Reportes-------------------------#
        elif event == "Consultar reportes":
            print("Consultar reportes")
        elif event == "Exportar CSV":
            print(f"Archivo de reporte: {path_csv_report}")
        
        # ------------Configuracion del tema-------------------------#
        # Menú Configuración
        elif event == "Tema claro":
            current_theme = "LightBlue1"
            window.close()
            windows["main"] = create_main_window(
                current_theme,
                action
            )
            # window = create_main_window(current_theme,action)  

        elif event == "Tema oscuro":
            current_theme = "DarkGrey2"
            window.close()
            windows["main"] = create_main_window(
            current_theme,
            action
            )
            # window = create_main_window(current_theme,action)         
        
        # Codigo para evaluar los diferentes eventos en la ventana

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


        elif event == "Exportar Reporte":
                    print(f"Archivo de reporte: {path_csv_report}")
    # window.close()
    #====================================================================#
    # Esto garantiza que se cierren todas las ventanas registradas al salir
    #====================================================================#
    for open_window in list(windows.values()):
        open_window.close()

    windows.clear()