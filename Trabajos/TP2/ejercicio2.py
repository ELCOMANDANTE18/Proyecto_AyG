import re

numero_regex = r'^[-+]?[0-9]{1,3}(,[0-9]{3})*(\.[0-9]{2})?$'

while True:
    numero = input("Ingrese un número real con dos decimales y separador de miles (o escriba 'salir' para terminar): ")
    
    if numero.lower() == "salir":
        break
    
    if re.match(numero_regex, numero):
        print(f"{numero} es un número válido.")
    else:
        print(f"{numero} no es un número válido.")