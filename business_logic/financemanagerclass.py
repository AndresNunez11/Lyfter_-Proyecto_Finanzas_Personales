from datetime import datetime
from business_logic.categoryclass import Category 
from business_logic.movementclass import Movement
from business_logic.categoryjsonfile import category_read_json_file, category_save_json_file
from business_logic.movementjsonfile import movement_read_json_file, movement_save_json_file


class categoryexistserror(Exception):
    def __init__(self):
        super().__init__("Ya existe una categoría con ese nombre")

class finance_manager:
    def __init__(self,path_categories, path_movements, path_csv):
        self.path_categories = path_categories
        self.path_movements = path_movements
        self.path_csv = path_csv

        # Cargar los datos una sola vez
        self.categories:list[Category] = category_read_json_file(self.path_categories)
        self.movements:list[Movement] = movement_read_json_file(self.path_movements)

    def add_category(self, category:Category):
        # self.categories = category_read_json_file(path_json_file) #Se iguala para que entienda que es una lista de categorias
        for exist_category in self.categories:
            if exist_category.name.lower() == category.name.lower():
                raise categoryexistserror()
        self.categories.append(category)
        category_save_json_file(self.categories, self.path_categories)
        print(f'Categorias: \n{self.categories}')
        return self.categories

    def add_movement(self, movement:Movement):
        # self.movements = movement_read_json_file(path_json_file)
        print(f'Movimientos \n {self.movements}\n')
        self.movements.append(movement)
        movement_save_json_file(self.movements, self.path_movements)
        return self.movements

    def list_category(self):
        categories = self.categories #Se iguala para que entienda que es una lista de categorias
        return [category.name for category in categories]
    

    def filter_category(self, category_name):
        self.categories = self.categories
        for exist_category in self.categories:
            if exist_category.name.lower() == category_name.lower():
                return exist_category

    def list_movement(self):
        movements = self.movements
        return movements

    def incoming_balance(self):
        incoming_amount = 0
        movements = self.movements
        for movement in movements:
            if(movement.type == "Ingreso"):
                incoming_amount+=movement.amount
        return incoming_amount    

    def expense_balance(self):
            expense_amount = 0
            movements = self.movements
            for movement in movements:
                if(movement.type == "Gasto"):
                    expense_amount+=movement.amount
            return expense_amount 

    def global_balance(self):
        expense_amount = self.expense_balance()
        incoming_amount = self.incoming_balance()
        balance = incoming_amount-expense_amount
        return balance

    def filter_movements_by_date_range(self, start_date, end_date):
        movements = self.movements
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
            
            
            

