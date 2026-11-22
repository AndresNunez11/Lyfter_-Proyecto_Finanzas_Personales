from business_logic.categoryclass import Category
from business_logic.financemanagerclass import FinanceManager, CategoryExistsError
from business_logic.categoryvalidationclass import FormatTypeError, NameTypeError, EmptyTypeError
import pytest 

#python -m pytest -v qa_test/ comando para ejecutar las pruebas desde la carpeta.

def test_add_new_category_correct_category(tmp_path):
    #Arrange
    path_categories = tmp_path / "categories.json"
    path_movements = tmp_path / "movements.json"
    path_csv = tmp_path / "report.csv"
    action = FinanceManager(
        path_categories,
        path_movements,
        path_csv
    )    
    new_category = Category('Trabajo','#000000')
    # path_json_file =  tmp_path / "test_categories.json"
    #Act
    Result = action.add_category(new_category) 
    #Assert
    assert len(Result) == 1
    assert Result[0].name == "Trabajo"
    assert Result[0].color == "#000000"

def test_add_duplicate_category(tmp_path):
    # Arrange
    path_categories = tmp_path / "categories.json"
    path_movements = tmp_path / "movements.json"
    path_csv = tmp_path / "report.csv"
    actions = FinanceManager(
        path_categories,
        path_movements,
        path_csv
    ) 
    category1 = Category("Trabajo", "#000000")
    category2 = Category("Trabajo", "#FFFFFF")
    # path_json_file = tmp_path / "test_categories.json"
    actions.add_category(category1)
    # Act + Assert
    with pytest.raises(CategoryExistsError):
        actions.add_category(category2)

def test_add_category_wrong_color_format():
    # Arrange
    name = "Trabajo"
    color = "aa00000"
    # Act + Assert
    with pytest.raises(FormatTypeError):
        Category(name, color)

def test_add_category_empty_name():
    # Arrange
    name = ""
    color = "#FFFFFF"
    # Act + Assert
    with pytest.raises(EmptyTypeError):
        Category(name, color)

def test_add_category_number_name():
    # Arrange
    name = "234Trabajo"
    color = "#000000"
    # Act + Assert
    with pytest.raises(NameTypeError):
        Category(name, color)





