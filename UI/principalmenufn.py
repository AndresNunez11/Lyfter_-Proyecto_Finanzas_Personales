import FreeSimpleGUI as sg
from UI.createmainwindowtype import create_main_window
from business_logic.financemanagerclass import finance_manager
from datetime import datetime
from UI.movementtablefn import movement_table, movement_table_data
from UI.createcategorywindowtype import create_category_window


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
        # ------------Categorias-------------------------#
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
        elif event == "-SAVE-CATEGORY-":
            name = values["-CATEGORY-NAME-"]
            color = values["-CATEGORY-COLOR-"]
            print("Nombre:", name)
            print("Color:", color)

        # ------------MOvimientos-------------------------#
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
            window = create_main_window(current_theme,action)  
        elif event == "Tema oscuro":
            current_theme = "DarkGrey2"
            window.close()
            window = create_main_window(current_theme,action)         
        
        # Codigo para evaluar los diferentes eventos en la ventana
        # Menu para elegir si la tabla de movimientos se debe filtrar o no 
        elif event == "-ENABLE-FILTER-":
            enabled = values["-ENABLE-FILTER-"]

            # Mostrar u ocultar todos los controles de fecha
            filter_elements = [
                "-START-LABEL-",
                "-START-DATE-",
                "-START-CALENDAR-",
                "-END-LABEL-",
                "-END-DATE-",
                "-END-CALENDAR-",
                "-FILTER-DATES-"
            ]

            for key in filter_elements:
                window[key].update(visible=enabled)

            if not enabled:
                # Restaurar todos los movimientos
                table_values, row_colors = movement_table_data(
                    action.movements
                )

                window["-MOVEMENTS-TABLE-"].update(
                    values=table_values,
                    row_colors=row_colors
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