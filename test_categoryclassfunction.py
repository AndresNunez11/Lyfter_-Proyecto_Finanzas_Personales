from categoryclass import Category
from financemanagerclass import finance_manager, CategoryExistsError
from categoryvalidationclass import FormatTypeError, NameTypeError, EmptyTypeError
import pytest 

def test_add_new_category_correct_category(tmp_path):
    #Arrange
    action = finance_manager()
    new_category = Category('Trabajo','#000000')
    path_json_file =  tmp_path / "test_categories.json"
    #Act
    Result = action.add_category(new_category, path_json_file) 
    #Assert
    assert len(Result) == 1
    assert Result[0].name == "Trabajo"
    assert Result[0].color == "#000000"

def test_add_duplicate_category(tmp_path):
    # Arrange
    actions = finance_manager()
    category1 = Category("Trabajo", "#000000")
    category2 = Category("Trabajo", "#FFFFFF")
    path_json_file = tmp_path / "test_categories.json"
    actions.add_category(category1, path_json_file)
    # Act + Assert
    with pytest.raises(CategoryExistsError):
        actions.add_category(category2, path_json_file)

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





