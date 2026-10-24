import FreeSimpleGUI as sg
from UI.financialindicatorsfn import create_financial_indicators
from UI.movementtablefn import movement_table
from UI.filtermovementfn import filter_table
from business_logic.financemanagerclass import finance_manager
from UI.footerfn import create_footer

#Funcion para la pantalla principal
def create_main_window(theme,action:finance_manager):

    sg.theme(theme)
    menu_definition = [
        ["Inicio", ["Principal", "Salir"]],
        ["Administración", ["Categorías", "Movimientos"]],
        ["Reportes", ["Consultar reportes", "Exportar CSV"]],
        ["Configuración", ["Tema claro", "Tema oscuro"]]
    ]

    indicators = create_financial_indicators(action)
    footer = create_footer()
    filter_movement_list = filter_table()
    w_movement_table = movement_table(action) 
    

    layout = [
        [sg.Menu(menu_definition,
                key="-MENU-",
                font=("Arial", 14))],
        [
        sg.Push(),
        sg.Button("☀ Claro", key="Tema claro", size=(8,0), font=("Arial", 12, "bold")),
        sg.Button("🌙 Oscuro", key="Tema oscuro", size=(8,0), font=("Arial", 12, "bold") ),
        sg.Button("Salir", size=(8,0), font=("Arial", 12, "bold"))
        ],
        [sg.Text("GESTIÓN DE FINANZAS PERSONALES", font=("Arial", 20, "bold"))],
        [sg.HorizontalSeparator()],
        [sg.Column
            (
                [
                    [sg.Frame(
                        "Bienvenido a IQ - Smart Finance",
                        [
                        [sg.Text("", background_color="#475569", size=(1, 1))], #size=(1, 2) agrega una fila vacía de aproximadamente dos líneas de alto
                        [   
                        sg.Push(background_color="#475569"),
                        sg.Button("Categorías", size=(15, 1)),
                        sg.Button("Movimientos", size=(15, 1)),
                        sg.Button("Exportar Reporte", size=(15, 1)),
                        sg.Push(background_color="#475569")
                        ],
                        ],
                        title_color="#F8FAFC",
                        title_location="n",
                        element_justification="center",
                        background_color="#475569",
                        expand_x=True,
                        relief="flat",
                        size=(1250, 200),
                        pad=((20, 20), (40, 40))
                        )
                    ],
                    [sg.HorizontalSeparator()],
                    [sg.Column
                        ([indicators],
                        expand_x=True,
                        expand_y=True,
                        pad=(0,0))
                    ],
                    [sg.HorizontalSeparator()],
                    [filter_movement_list],
                    [w_movement_table]
                ],
            scrollable=True,
            vertical_scroll_only=True,
            # size=(1260, 600),
            expand_x=True,
            expand_y=True,
            key="-SCROLL-",
            pad=(0,0),
            # background_color="#1F2937"
            )   
        ],
        [footer]
    ] 
    window = sg.Window("IQ - Smart Finance", 
                    layout, 
                    size=(1300, 650), 
                    resizable=True, 
                    finalize=True,
                    margins=(0, 0),
                    # background_color="#1F4E78",
                    font=("Arial", 20, "bold"))
    return window  