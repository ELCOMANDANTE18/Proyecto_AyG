import re

cuil_regex = r"^(20|23|24|27|30)(\d{8})([0-9])$"

while True:
    cuil = input("Ingrese un CUIL o 'salir' para terminar: ")
    if cuil.lower() == "salir":
        break

    if re.match(cuil_pattern, cuil):
        print(f"{cuil} es un CUIL válido.")
    else:
        print(f"{cuil} no es un CUIL válido.")