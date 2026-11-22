import FreeSimpleGUI as sg
from business_logic.financemanagerclass import FinanceManager
from business_logic.categoryclass import Category



def create_add_movement_window(theme, action:FinanceManager):
    sg.theme(theme)
    categories = action.categories

    category_names = [
        category.name
        for category in categories
    ]
    # type_names = ['ingreso', 'gasto']

    layout = [
            [[sg.Text("Ingrese un nuevo movimiento", font=("Arial", 14, "bold"))]],
            [[sg.HorizontalSeparator()]],
            #========================
            #------FECHA-------
            #========================
            [
            sg.Text("Fecha:", key="-DATE-MOVEMENT-LABEL-", visible=True, size =(10,1)),                            
            sg.Input(
                key="-MOVEMENT-DATE-",
                size=(18, 1),
                visible=True,
            ),
            sg.Button(
                "📅",
                key="-PICK-MOVEMENT-DATE-",
                visible=True
            ),
            ],
            #========================
            #------DESCRIPCION-------
            #========================
            [
            sg.Text("Descripción:", key="-DESCRIPTION-MOVEMENT-LABEL-", visible=True, size =(10,1)),                            
            sg.Input(
                key="-DESCRIPTION-MOVEMENT-",
                size=(18, 3),
                visible=True
            ),
            ],
            #========================
            #------MONTO-------
            #========================
            [
            sg.Text("Monto:", key="-AMOUNT-MOVEMENT-LABEL-", visible=True, size =(10,1)),
            sg.Input(
                key="-AMOUNT-MOVEMENT-",
                size=(18, 1),
                visible=True
            ),
            ],
            #========================
            #------CATEGORIA-------
            #========================
            [
            sg.Text("Categoria:", key="-CATEGORY-MOVEMENT-LABEL-", visible=True, size =(10,1)), 
            sg.Combo(
                category_names,
                size=(18, 1),
                key="-PICK-CATEGORY-MOVEMENT-",
                readonly=True,
                enable_events=True
            )                           
            ],
            #========================
            #------TIPO------- se pasa fijo al elegir el tipo de movimiento
            #========================
            [
                sg.Push(),
                sg.Button(
                    "Agregar",
                    key="-PICK-ADD-MOVEMENT-",
                    visible=True
                    ),
                sg.Button(
                    "Cerrar",
                    key="-CLOSE-MOVEMENT-",
                    visible=True
                ),
                sg.Push()
            ]         
            
        ]
    window = sg.Window("IQ - Smart Finance/Categorias", 
                            layout, 
                            size=(400, 300), 
                            resizable=True, 
                            finalize=True,
                            margins=(0, 0),
                            # background_color="#1F4E78",
                            font=("Arial", 15, "bold"))
    return window  