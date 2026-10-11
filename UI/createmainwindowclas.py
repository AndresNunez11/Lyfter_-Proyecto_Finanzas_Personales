import FreeSimpleGUI as sg



#Uso de tkinter.Canvas para conseguir un panel con esquinas redondeadas
# def draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25,
#     fill="#475569", outline=""):
#     points = [
#         x1 + radius, y1,
#         x2 - radius, y1,
#         x2, y1,
#         x2, y1 + radius,
#         x2, y2 - radius,
#         x2, y2,
#         x2 - radius, y2,
#         x1 + radius, y2,
#         x1, y2,
#         x1, y2 - radius,
#         x1, y1 + radius,
#         x1, y1
#     ]
#     canvas.create_polygon(
#         points,
#         smooth=True,
#         splinesteps=36,
#         fill=fill,
#         outline=outline
#     )

#     canvas.create_text(
#     470, 35,
#     text="Bienvenido a IQF - Smart Finance",
#     font=("Arial", 16, "bold"),
#     fill="#F8FAFC",
#     anchor="center"
#     )


#Funcion para la pnatalla principal
def create_main_window(theme):

    sg.theme(theme)
    menu_definition = [
        ["Inicio", ["Principal", "Salir"]],
        ["Administración", ["Categorías", "Movimientos"]],
        ["Reportes", ["Consultar reportes", "Exportar CSV"]],
        ["Configuración", ["Tema claro", "Tema oscuro"]]
    ]

    layout = [
        [sg.Menu(menu_definition,
                key="-MENU-",
                font=("Arial", 14))],
        [
        sg.Push(),
        sg.Button("☀ Claro", key="-LIGHT-", size=(8,0), font=("Arial", 12, "bold")),
        sg.Button("🌙 Oscuro", key="-DARK-", size=(8,0), font=("Arial", 12, "bold") ),
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
                        # [
                        #     sg.Text(
                        #         "Selecciona el módulo que deseas utilizar",
                        #         font=("Arial", 12),
                        #         justification="left",
                        #         text_color="#A7F3D0",
                        #         background_color="#475569",
                        #         expand_x=True,
                        #         relief="flat"
                        #     )
                        # ],
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
        # [sg.Canvas(
        #     size=(1000, 250),
        #     key="-PANEL-",
        #     expand_x=True,
        #     expand_y=True,
        #     pad=(20, 20)
        #     )
        # ],
    ] 

    window = sg.Window("IQF - Smart Finance", 
                    layout, 
                    size=(1300, 750), 
                    resizable=True, 
                    finalize=True,
                    margins=(0, 0),
                    # background_color="#1F4E78",
                    font=("Arial", 20, "bold"))

    # canvas = window["-PANEL-"].TKCanvas

    # draw_rounded_rectangle(
    #     canvas,
    #     10, 10, 930, 220,
    #     radius=25,
    #     fill="#475569"
    # )

    return window  
    
    # return sg.Window("IQF - Smart Finance", 
    #                 layout, 
    #                 size=(1000, 500), 
    #                 resizable=False, 
    #                 finalize=True,
    #                 # background_color="#1F4E78",
    #                 font=("Arial", 20, "bold"))