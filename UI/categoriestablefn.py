import FreeSimpleGUI as sg
from business_logic.financemanagerclass import finance_manager


def category_table_data(categories):
    values = []
    row_colors = []
    # print(categories)
    # input('Espera de resultado')

    for index, category in enumerate(categories):
        values.append([
            category.name,
            category.color
        ])

        # El color de la categoría se usa como fondo de la fila.
        background = category.color
        text_color = "#FFFFFF"

        row_colors.append((index, background, text_color))

    return values, row_colors

def categories_table(action: finance_manager):
        values, row_colors = category_table_data(action.categories)

        return sg.Table(
            values=values,
            headings=[
                "Categoria",
                "Color",
            ],
            key="-CATEGORIES-TABLE-",
            size=(900,10),
            # auto_size_columns=True,
            col_widths=[12, 12],
            justification="left",
            num_rows=10,
            expand_x=True,
            expand_y=True,
            row_colors=row_colors,
            enable_events=True
            )

