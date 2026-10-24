import re
from datetime import date, datetime

#Clase para que la descripcion de la categoria no incluya un numero
class NameTypeError(Exception):
    def __init__(self):
        super().__init__(f'\n El dato ingresado no puede ser o incluir un número')

#Clase para que el nombre no puede estar vacio
class EmptyTypeError(Exception):
    def __init__(self):
        super().__init__(f'\n El dato no puede estar vacio')

class FormatError(Exception):
    def __init__(self):
        super().__init__(f'\n La fecha no puede ser posterior al dia de hoy')


class movement_validation:

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
    
    # Exception Negative Number
    @staticmethod
    def no_negative_number(enter_number):
        if int(enter_number) < 0:
            raise ValueError("El número no puede ser menor que cero")
        return enter_number

    # Exception para validar que la fecha no sea mayor a hoy
    @staticmethod
    def validate_date(input_date):
        formats = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d"]
        for format in formats:
            try:
                date_m = datetime.strptime(input_date, format).date()
                if date_m > date.today():
                    raise FormatError()
                return date_m
            except ValueError:
                continue
        raise ValueError("Formato de fecha inválido. Use DD-MM-YYYY")

    # Exception para validar que el tipo de movimiento este correcto
    @staticmethod
    def validate_type(input_text):
        input_text = input_text.strip().lower()
        if input_text not in ['ingreso', 'gasto']:
            raise ValueError("El tipo debe ser Ingreso o Gasto")
        input_text = input_text.capitalize()
        return input_text
        
        

