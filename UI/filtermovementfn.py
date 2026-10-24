
import FreeSimpleGUI as sg


def filter_table():
    filter_layout = [
        [
            sg.Checkbox(
                "Filtrar por fecha",
                key="-ENABLE-FILTER-",
                enable_events=True,
                default=False
            )
        ],
        [
            sg.Text("Fecha inicio:", key="-START-LABEL-", visible=False),
            sg.Input(
                key="-START-DATE-",
                size=(12, 1),
                visible=False,
                readonly=True
            ),
            sg.CalendarButton(
                "Seleccionar",
                target="-START-DATE-",
                format="%d/%m/%Y",
                key="-START-CALENDAR-",
                visible=False
            ),
            sg.Text("Fecha fin:", key="-END-LABEL-", visible=False),
            sg.Input(
                key="-END-DATE-",
                size=(12, 1),
                visible=False,
                readonly=True
            ),
            sg.CalendarButton(
                "Seleccionar",
                target="-END-DATE-",
                format="%d/%m/%Y",
                key="-END-CALENDAR-",
                visible=False
            ),
            sg.Button(
                "Filtrar",
                key="-FILTER-DATES-",
                visible=False
            )
        ]
    ]

    return sg.Column(
        filter_layout,
        key="-FILTER-TABLE-",
        expand_x=True,
        pad=(5, 5)
    )
