import re

ar_phone_regex = r'^(\+54|54|0)?(11|[2-9][0-9]{2})(15)[0-9]{6}$'

while True:
    ar_phone = input("Ingrese un número de teléfono móvil de Argentina que incluya código de país, de provincia y el 15 (o escriba 'salir' para terminar): ")
    
    if ar_phone.lower() == "salir":
        break
    
    if re.match(ar_phone_regex, ar_phone):
        print(f"{ar_phone} es un número de teléfono móvil de Argentina válido.")
    else:
        print(f"{ar_phone} no es un número de teléfono móvil de Argentina válido.")