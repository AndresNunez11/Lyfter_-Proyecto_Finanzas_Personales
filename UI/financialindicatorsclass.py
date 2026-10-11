
import FreeSimpleGUI as sg


def create_financial_indicators():

    balance = 0
    income = 0
    expenses = 0



    card_balance = sg.Frame(
        "BALANCE",
        [
            [
                sg.Text(
                    str(balance),
                    key="-BALANCE-",
                    font=("Arial", 20, "bold"),
                    background_color="#DBEAFE",
                    text_color="#1E3A8A",
                    expand_x=True,
                    justification="center"
                )
            ],
            [
                sg.Text(
                    "Ingresos - gastos",
                    background_color="#DBEAFE",
                    text_color="#1E3A8A",
                    justification="center",
                    expand_x=True
                )
            ]
        ],
        background_color="#DBEAFE",
        title_color="#1E3A8A",
        element_justification="center",
        expand_x=True,
        relief="flat",
        pad=(10, 10)
    )

    card_income = sg.Frame(
        "TOTAL DE INGRESOS",
        [
            [
                sg.Text(
                    str(income),
                    key="-INCOME-",
                    font=("Arial", 20, "bold"),
                    background_color="#D1FAE5",
                    text_color="#065F46",
                    justification="center",
                    expand_x=True
                )
            ],
            [
                sg.Text(
                    "Dinero recibido",
                    background_color="#D1FAE5",
                    text_color="#065F46",
                    justification="center",
                    expand_x=True
                )
            ]
        ],
        background_color="#D1FAE5",
        title_color="#065F46",
        element_justification="center",
        expand_x=True,
        relief="flat",
        pad=(10, 10)
    )

    card_expenses = sg.Frame(
        "TOTAL DE GASTOS",
        [
            [
                sg.Text(
                    str(expenses),
                    key="-EXPENSES-",
                    font=("Arial", 20, "bold"),
                    background_color="#FEE2E2",
                    text_color="#991B1B",
                    justification="center",
                    expand_x=True
                )
            ],
            [
                sg.Text(
                    "Dinero gastado",
                    background_color="#FEE2E2",
                    text_color="#991B1B",
                    justification="center",
                    expand_x=True
                )
            ]
        ],
        background_color="#FEE2E2",
        title_color="#991B1B",
        element_justification="center",
        expand_x=True,
        relief="flat",
        pad=(10, 10)
    )

    return [
        card_balance,
        card_income,
        card_expenses
    ]