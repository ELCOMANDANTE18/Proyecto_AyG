import re

um_email_regex = r'^[a-z]+\.[a-z]+[0-9]{0,3}@alumno\.um\.edu\.ar$'

while True:
    um_email = input("Ingrese una cuenta de email de un alumno de la Universidad de Mendoza (o escriba 'salir' para terminar): ")
    
    if um_email.lower() == "salir":
        break
    
    if re.match(um_email_regex, um_email):
        print(f"{um_email} es una cuenta de email válida de un alumno de la Universidad de Mendoza.")
    else:
        print(f"{um_email} no es una cuenta de email válida de un alumno de la Universidad de Mendoza.")