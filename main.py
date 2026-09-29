from menu import menu

# Variables Globales
#Utilizar la variable global en la mayuscula cuando es inmutable -- 
PATH_JSON_CAT = 'jsoncategoriesfile.json'
PATH_JSON_MOV = 'jsonmovementsfile.json'
PATH_CSV_REPORT = 'Lyfter_Gestor_Finanzas_Personales/REPORT.csv'

#Funcion principal del sistema 
def main(PATH_JSON_CAT, PATH_JSON_MOV, PATH_CSV_REPORT):
    try:
        menu(PATH_JSON_CAT, PATH_JSON_MOV, PATH_CSV_REPORT)
    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')

#Inicio del Sistema
if __name__ == "__main__":
    main(PATH_JSON_CAT, PATH_JSON_MOV, PATH_CSV_REPORT)