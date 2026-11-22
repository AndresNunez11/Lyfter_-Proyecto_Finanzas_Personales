import FreeSimpleGUI as sg
from business_logic.financemanagerclass import FinanceManager
from UI.categoriestablefn import categories_table
from UI.footerfn import create_footer

# ======================================================================================
#Funcion para la pantalla principal
# ======================================================================================

def create_category_window(theme,action:FinanceManager):
    sg.theme(theme)
    menu_definition = [
            ["Inicio", ["Principal", "Salir"]],
            ["Administración", ["Agregar Categoria", "Modificar Categoria"]],
            ["Configuración", ["Tema claro", "Tema oscuro"]]
        ]
    # ======================================================================================
    #===========================Objetos=================================#
    # ======================================================================================

    footer = create_footer()
    categories = categories_table(action)
    # ======================================================================================
    # ---------------------Layout-----------------------------------------------------------
    # ======================================================================================
    
    
    layout = [
        [sg.Menu(menu_definition,
                key="-MENU-",
                font=("Arial", 14))
        ],
        [sg.Text("Administración Categorias", font=("Arial", 20, "bold"))],
                [sg.Column
                    (
                        [
                            [sg.HorizontalSeparator()],
                            [sg.Frame(
                                "Categorias - IQ - Smart Finance",
                                [],
                                title_color="#F8FAFC",
                                title_location="n",
                                element_justification="center",
                                background_color="#475569",
                                expand_x=True,
                                relief="flat",
                                size=(900, 30),
                                pad=((10, 10), (10, 10))
                                )
                            ],
                            [sg.HorizontalSeparator()],
                        ],
                    vertical_scroll_only=True,
                    expand_x=True,
                    expand_y=True,
                    key="-SCROLL-",
                    pad=(0,0),
                    )   
                ],
                [categories],
                [
                sg.Button(
                        "Agregar",
                        key="-ADD-CATEGORY-"
                        ),
                sg.Push(),
                sg.Button(
                        "Cerrar",
                        key="-CLOSE-CATEGORY-"
                        )
                ],
                [footer]

            ] 
    window = sg.Window("IQ - Smart Finance/Categorias", 
                        layout, 
                        size=(900, 550), 
                        resizable=True, 
                        finalize=True,
                        margins=(0, 0),
                        font=("Arial", 15, "bold"))
    return window  