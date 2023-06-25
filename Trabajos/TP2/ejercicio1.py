import re

fecha_regex = r'\d{2}[-/]\d{2}[-/]\d{4}'

while True:
    fecha = input("Ingrese una fecha con formato dd/mm/yyyy o dd-mm-yyyy (o escriba 'salir' para terminar): ")

    if fecha.lower() == "salir":
        break

    if re.match(fecha_regex, fecha):
        print(f"{fecha} es una fecha válida.")
    else:
        print(f"{fecha} no es una fecha válida.")