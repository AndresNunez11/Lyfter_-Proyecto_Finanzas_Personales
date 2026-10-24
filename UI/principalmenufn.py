import FreeSimpleGUI as sg
from UI.createmainwindowtype import create_main_window
from business_logic.financemanagerclass import finance_manager
from datetime import datetime
from UI.movementtablefn import movement_table, movement_table_data


def principal_menu_GUI(path_json_cat, path_json_mov, path_csv_report, theme):

    action = finance_manager(path_json_cat, path_json_mov,path_csv_report)
    current_theme = theme
    window = create_main_window(current_theme,action)

    # Iniciamos el Event Loop
    while True:
        # El programa se "detiene" aquí (bloqueo) esperando una acción
        event, values = window.read()
        # Si el usuario cierra la ventana, rompemos el ciclo
        if event in (sg.WINDOW_CLOSED, "Salir"):
            break
        # Menú Inicio
        elif event == "Principal":
            print("Mostrar pantalla principal")
        elif event == "Salir":
            break
        # Menú Administración
        elif event == "Categorías":
            print("Abrir gestión de categorías")
        elif event == "Movimientos":
            print("Abrir gestión de movimientos")
        
        # Menú Reportes
        elif event == "Consultar reportes":
            print("Consultar reportes")
        elif event == "Exportar CSV":
            print(f"Archivo de reporte: {path_csv_report}")
        
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
    window.close()