from business_logic.movementclass import Movement
from business_logic.movementsvalidationclass import EmptyTypeError, FormatError
from business_logic.financemanagerclass import FinanceManager
from business_logic.categoryclass import Category
from datetime import date
import pytest

def test_add_correct_movement(tmp_path):
    #Arrange
    path_categories = tmp_path / "categories.json"
    path_movements = tmp_path / "movements.json"
    path_csv = tmp_path / "report.csv"
    action = FinanceManager(
        path_categories,
        path_movements,
        path_csv
    )
    m_date =  '28-09-2026'
    description = 'Pago de salario'
    amount = 1500000.0
    category = Category('Salario','#000000')
    m_type = 'Ingreso'
    new_movement = Movement(m_date, description, amount, category, m_type)
    #Act
    Result = action.add_movement(new_movement) 
    #Assert
    assert len(Result) == 1
    assert Result[0].date ==  date(2026, 9, 28)
    assert Result[0].description == "Pago de salario"
    assert Result[0].amount == 1500000.0
    assert Result[0].category.name  == "Salario"
    assert Result[0].category.color == "#000000"
    assert Result[0].type == "Ingreso"

def test_add_empty_description_movement():
    #Arrange
    m_date =  '28-09-2026'
    description = ''
    amount = 1500000.0
    category = Category('Salario','#000000')
    m_type = 'Ingreso'
    #Act
    with pytest.raises(EmptyTypeError):
        Movement(m_date, description, amount, category, m_type)

def test_add_wrong_format_date_movement():
    #Arrange
    m_date =  '20-09-28'
    description = 'Pago de Salario'
    amount = 1500000.0
    category = Category('Salario','#000000')
    m_type = 'Ingreso'
    #Act
    with pytest.raises(ValueError):
        Movement(m_date, description, amount, category, m_type)

def test_add_wrong_date_after_today_movement():
    #Arrange
    m_date =  '2028-09-30'
    description = 'Pago de Salario'
    amount = 1500000.0
    category = Category('Salario','#000000')
    m_type = 'Ingreso'
    #Act
    with pytest.raises(FormatError):
        Movement(m_date, description, amount, category, m_type)

def test_add_negative_amount_wrong_movement():
    #Arrange
    m_date =  '28-09-2026'
    description = 'Pago de Salario'
    amount = -1500000.0
    category = Category('Salario','#000000')
    m_type = 'Ingreso'
    #Act
    with pytest.raises(ValueError):
        Movement(m_date, description, amount, category, m_type)     

def test_add__wrong_type_movement():
    #Arrange
    m_date =  '28-09-2026'
    description = 'Pago de Salario'
    amount = 1500000.0
    category = Category('Salario','#000000')
    m_type = 'Salario'
    #Act
    with pytest.raises(ValueError):
        Movement(m_date, description, amount, category, m_type)  