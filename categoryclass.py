from categoryvalidationclass import category_validation

class Category:

    def __init__(self, name, color="#FFFFFF"):
        self.name = name
        self.color = color

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = category_validation.validate_empty_name(category_validation.validate_name(name))
        
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = category_validation.validate_color_format(color)

    def __str__(self):
        return f"Categoría: {self.name} | Color: {self.color}"

    def __repr__(self):
        return f"Category(name='{self.name}', color='{self.color}')"

    # Lo convierte en un diccionario para poder llevarlo al formato Json
    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color
        }
