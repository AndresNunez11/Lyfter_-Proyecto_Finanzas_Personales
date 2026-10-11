import re

#Clase para que la descripcion de la categoria no incluya un numero
class NameTypeError(Exception):
    def __init__(self):
        super().__init__(f'\n El titulo no puede ser o incluir un número')

#Clase para que el nombre no puede estar vacio
class EmptyTypeError(Exception):
    def __init__(self):
        super().__init__(f'\n El dato no puede esta vacio')


#Clase para que el formato del color sea el correcto
class FormatTypeError(Exception):
    def __init__(self):
        super().__init__(f'\n El formato del color es incorrecto, debe de coincier con un codigo hexadecimal de color')



class category_validation:

    #Excepcion para validar el nombre de la categoria no tenga un numero
    @staticmethod
    def validate_name(name):
        if any(char.isdigit() for char in name):
            raise NameTypeError()
        return name

    #Excepcion para validar el nombre de la categoria no este vacio
    @staticmethod
    def validate_empty_name(name):
        if name.strip() == "":
            raise EmptyTypeError()
        return name

    #Excepcio para validar el formato del color
    @staticmethod
    def validate_color_format(enter_text):
        patron = r"^#[0-9A-Fa-f]{6}$"
        if bool(re.match(patron, enter_text)):
            return enter_text
        raise FormatTypeError
    
        
        

