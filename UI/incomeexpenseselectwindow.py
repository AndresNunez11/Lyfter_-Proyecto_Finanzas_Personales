import FreeSimpleGUI as sg

def create_select_expense_income_window(theme):
    sg.theme(theme)
    layout = [
            [[sg.Text("Seleccione el tipo de movimiento", font=("Arial", 14, "bold"))]],
            [[sg.HorizontalSeparator()]],
            [
                sg.Push(),
                sg.Button(
                    "Gasto",
                    key="-PICK-EXPENSE-",
                    visible=True
                    ),
                sg.Button(
                    "Ingreso",
                    key="-PICK-INCOME-",
                    visible=True
                ),
                sg.Button(
                    "Cerrar",
                    key="-CLOSE-EXPENSE_INCOME-",
                    visible=True
                ),
                sg.Push()
            ]         
            
        ]
    window = sg.Window("IQ - Smart Finance/Categorias", 
                            layout, 
                            size=(350, 100), 
                            resizable=True, 
                            finalize=True,
                            margins=(0, 0),
                            # background_color="#1F4E78",
                            font=("Arial", 15, "bold"))
    return window  