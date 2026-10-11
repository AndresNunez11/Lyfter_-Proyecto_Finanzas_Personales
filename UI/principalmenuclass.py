import FreeSimpleGUI as sg
from UI.createmainwindowclas import create_main_window


def principal_menu_GUI(path_json_cat, path_json_mov, path_csv_report, theme):
    
    current_theme = theme
    window = create_main_window(current_theme)

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
            window = create_main_window(current_theme)
            print("Ventana:", window.size)
            print("Columna:", window["-SCROLL-"].get_size())
        elif event == "Tema oscuro":
            current_theme = "DarkGrey2"
            window.close()
            window = create_main_window(current_theme)
        # Codigo para evaluar los diferentes eventos en la ventana
        if event == "-LIGHT-":
            window.close()
            current_theme = "LightBlue1"
            window = create_main_window(current_theme)
        if event == "-DARK-":
            window.close()
            current_theme = "DarkGrey2"
            window = create_main_window(current_theme)        
    window.close()