from datetime import datetime
from businesslogic.categoryclass import Category 
from businesslogic.movementclass import Movement
from businesslogic.categoryjsonfile import category_read_json_file, category_save_json_file
from businesslogic.movementjsonfile import movement_read_json_file, movement_save_json_file


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

    def list_movement(self, path_json_file):
        movements = movement_read_json_file(path_json_file)
        return movements

    def incoming_balance(self,path_json_file):
        incoming_amount = 0
        movements = movement_read_json_file(path_json_file)
        for movement in movements:
            if(movement.type == "Ingreso"):
                incoming_amount+=movement.amount
        return incoming_amount    

    def expense_balance(self,path_json_file):
            expense_amount = 0
            movements = movement_read_json_file(path_json_file)
            for movement in movements:
                if(movement.type == "Gasto"):
                    expense_amount+=movement.amount
            return expense_amount 

    def Global_balance(self,path_json_file):
        expense_amount = self.expense_balance(path_json_file)
        incoming_amount = self.incoming_balance(path_json_file)
        balance = incoming_amount-expense_amount
        return balance

    def filter_movements_by_date_range(self, start_date, end_date, path_json_file):
        movements = movement_read_json_file(path_json_file)
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        filtered_movements = []
        for movement in movements:
            movement_date = datetime.strptime(
                str(movement.date),
                "%Y-%m-%d"
            ).date()
            if start_date <= movement_date <= end_date:
                filtered_movements.append(movement)
        return filtered_movements
            
            
            

