
import FreeSimpleGUI as sg


def create_add_category_window(theme):
    sg.theme(theme)
    layout = [
            [[sg.Text("Ingrese nueva Categoria", font=("Arial", 14, "bold"))]],
            [[sg.HorizontalSeparator()]],
            [
                sg.Text("Categoria:", key="-NAME-CATEGORY-LABEL-", visible=True, size =(10,1)),                            
                sg.Input(
                    key="-CATEGORY-NAME-",
                    size=(12, 1),
                    visible=True,
                    ),

            ],
            [
                sg.Text("Color:", key="-COLOR-CATEGORY-LABEL-", visible=True, size =(10,1)),
                sg.Input(
                    key="-CATEGORY-COLOR-",
                    size=(12, 1),
                    visible=True,
                    ),
                sg.ColorChooserButton(
                    "Elegir color",
                    target="-CATEGORY-COLOR-",
                    font=("Arial", 8, "bold")
                    ),
            ],
            [
                sg.Push(),
                sg.Button(
                    "Agregar",
                    key="-PICK-ADD-CATEGORY-",
                    visible=True
                    ),
                sg.Push()
            ]         
            
        ]
    window = sg.Window("IQ - Smart Finance/Categorias", 
                            layout, 
                            size=(400, 200), 
                            resizable=True, 
                            finalize=True,
                            margins=(0, 0),
                            # background_color="#1F4E78",
                            font=("Arial", 15, "bold"))
    return window  