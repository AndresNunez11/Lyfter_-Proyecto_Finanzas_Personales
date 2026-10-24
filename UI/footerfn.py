import FreeSimpleGUI as sg


def create_footer():

    background = "#475569"
    text_color = "#E5E7EB"

    return [
        [
            sg.Column(
                [
                    [
                        sg.Text(
                            "© 2026 IQ - Smart Finance - Dev by Andres Nunez Solano",
                            text_color=text_color,
                            background_color=background,
                            font=("Arial", 9),
                            expand_x=True
                        ),
                        sg.Push(background_color=background),
                        sg.Text(
                            "Versión 1.0.0",
                            text_color=text_color,
                            background_color=background,
                            font=("Arial", 9)
                        )
                    ]
                ],
                background_color=background,
                expand_x=True,
                pad=(8, 8)
            )
        ]
    ]