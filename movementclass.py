from movementsvalidationclass import movement_validation
from categoryclass import Category

class Movement:

    def __init__(self, date, description, amount, category: Category, type):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category
        self.type = type

    @property 
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        self._date = movement_validation.validate_date(date)

    @property 
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
            self._description = movement_validation.validate_empty_name(description)

    @property 
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount):
        self._amount = movement_validation.no_negative_number(amount)

    @property 
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if not isinstance(category, Category):
            raise TypeError("La categoría debe ser un objeto Category")
        self._category = category

    @property 
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = movement_validation.validate_type(type)


    # Movimientos:- 02/07/2025 | Salario | ₡1000- 03/07/2025 | Comida | ₡-20
    # description, amount, category, type
    def __str__(self):
        return f"Movimiento:\n Fecha: {self.date} | Descripcion:{self.descripction} | Monto: {self.amount} | Categoria: {self.category} | Tipo: {self.type} \n"

    def __repr__(self):
        return f"Movimientos: (Fecha: '{self.date}' | Descripcion: '{self.descripction}' | Monto: '{self.amount}' | Categoria: '{self.category}' | Tipo: '{self.type}' )\n"

    # Lo convierte en un diccionario para poder llevarlo al formato Json
    def to_dict(self):
        return {
            "date": str(self.date), 
            "description": self.descripction, 
            "amount":str(self.amount), 
            "category": str(self.category),
            "type": self.type
        }