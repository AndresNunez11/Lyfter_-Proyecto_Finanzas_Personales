
import FreeSimpleGUI as sg
from business_logic.financemanagerclass import finance_manager


def movement_table_data(movements):
    values = []
    row_colors = []

    for index, movement in enumerate(movements):
        values.append([
            movement.date.strftime("%d/%m/%Y"),
            movement.description,
            movement.category.name,
            movement.type,
            f"₡{movement.amount:,.2f}"
        ])

        # El color de la categoría se usa como fondo de la fila.
        background = movement.category.color
        text_color = "#FFFFFF"

        row_colors.append((index, background, text_color))

    return values, row_colors


def movement_table(action: finance_manager):
    values, row_colors = movement_table_data(action.movements)

    return sg.Table(
        values=values,
        headings=[
            "Fecha",
            "Descripción",
            "Categoría",
            "Tipo",
            "Monto"
        ],
        key="-MOVEMENTS-TABLE-",
        auto_size_columns=True,
        col_widths=[12, 20, 20, 12, 15],
        justification="left",
        num_rows=15,
        expand_x=True,
        expand_y=True,
        row_colors=row_colors,
        enable_events=True
    )
