import FreeSimpleGUI as sg
from business_logic.financemanagerclass import finance_manager
from UI.categoriestablefn import categories_table
from UI.footerfn import create_footer

#Funcion para la pantalla principal
def create_category_window(theme,action:finance_manager):
    sg.theme(theme)
    menu_definition = [
            ["Inicio", ["Principal", "Salir"]],
            ["Administración", ["Agregar Categoria", "Modificar Categoria"]],
            ["Configuración", ["Tema claro", "Tema oscuro"]]
        ]
    
    #===========================Objetos=================================#
    footer = create_footer()
    categories = categories_table(action)

    #===================================================================#
    layout = [
        [sg.Menu(menu_definition,
                key="-MENU-",
                font=("Arial", 14))
        ],
        [sg.Text("Administración Categorias", font=("Arial", 20, "bold"))],
                [sg.HorizontalSeparator()],
                [sg.Column
                    (
                        [
                            [sg.Frame(
                                "Categorias - IQ - Smart Finance",
                                [
                                [sg.Text("", background_color="#475569", size=(1, 1))], #size=(1, 2) agrega una fila vacía de aproximadamente dos líneas de alto
                                [  
                                sg.Push(background_color="#475569"),
                                sg.Button("Ingresar Categoria", size=(25, 10), font=("Arial", 12, "bold")),
                                sg.Button("Mantenimiento a Categorias", size=(25, 10), font=("Arial", 12, "bold")),
                                sg.Push(background_color="#475569")
                                ],
                                ],
                                title_color="#F8FAFC",
                                title_location="n",
                                element_justification="center",
                                background_color="#475569",
                                expand_x=True,
                                relief="flat",
                                size=(900, 90),
                                pad=((10, 10), (10, 10))
                                )
                            ],
                            [sg.HorizontalSeparator()],
                            # [filter_movement_list],
                            # [w_movement_table]
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
                [categories],
        [footer]
        ] 
    window = sg.Window("IQ - Smart Finance/Categorias", 
                        layout, 
                        size=(900, 550), 
                        resizable=True, 
                        finalize=True,
                        margins=(0, 0),
                        # background_color="#1F4E78",
                        font=("Arial", 15, "bold"))
    return window  