import re

password_regex = r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$"

while True:
    password = input("Ingrese una contraseña o 'salir' para terminar: ")
    if password.lower() == "salir":
        break
    if re.match(password_regex, password):
        print(f"{password} es una contraseña segura.")
    else:
        print(f"{password} no es una contraseña segura.")