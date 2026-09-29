from categoryvalidationclass import category_validation

class Category:

    def __init__(self, name, color="#FFFFFF"):
        self.name = name
        self.color = color


# Propiedad name. El setter ejecuta las validaciones cuando se asigna un nombre.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = category_validation.validate_empty_name(category_validation.validate_name(name))

# Propiedad color. El setter ejecuta la validación del formato hexadecimal. 
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = category_validation.validate_color_format(color)



# Define la representación del objeto cuando se convierte a texto o se utiliza print().
    def __str__(self):
        return f"Categoría: {self.name} | Color: {self.color}"

# Define una representación técnica del objeto, útil para depuración y para mostrar objetos dentro de listas.
    def __repr__(self):
        return f"Category(name='{self.name}', color='{self.color}')"

#  Convierte el objeto en un diccionario para facilitar su serialización a formato JSON.
    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color
        }
