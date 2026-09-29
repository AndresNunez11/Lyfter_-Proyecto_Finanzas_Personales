from categoryclass import Category 
from movementclass import Movement
from categoryjsonfile import category_read_json_file, category_save_json_file
from movementjsonfile import movement_read_json_file, movement_save_json_file


class CategoryExistsError(Exception):
    def __init__(self):
        super().__init__("Ya existe una categoría con ese nombre")

class finance_manager:
    def __init__(self):
        self.categories:list[Category] = []
        self.movements:list[Movement] = []

    def add_category(self, category:Category, path_json_file):
        self.categories = category_read_json_file(path_json_file) #Se iguala para que entienda que es una lista de categorias
        for exist_category in self.categories:
            if exist_category.name.lower() == category.name.lower():
                raise CategoryExistsError()
        self.categories.append(category)
        category_save_json_file(self.categories, path_json_file)
        print(f'Categorias: \n{self.categories}')
        return self.categories

    def add_movement(self, movement:Movement, path_json_file):
        self.movements = movement_read_json_file(path_json_file)
        print(f'Movimientos \n {self.movements}\n')
        self.movements.append(movement)
        movement_save_json_file(self.movements, path_json_file)
        return self.movements

    def list_category(self, path_json_file ):
        categories = category_read_json_file(path_json_file) #Se iguala para que entienda que es una lista de categorias
        return [category.name for category in categories]

    def filter_category(self, category_name, path_json_file):
        self.categories = category_read_json_file(path_json_file)
        for exist_category in self.categories:
            if exist_category.name.lower() == category_name.lower():
                return exist_category

            
            

