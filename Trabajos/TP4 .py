def analisar(cadena, aceptar):
    print("+--------------+---------+-----------+---------------+")
    print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
    print("+--------------+---------+-----------+---------------+")
    razon = ""
    estado = "q1"
    cadena += "B"
    for caracter in cadena:
        if caracter not in caracteres:
            razon = f"\n{caracter} no es un caracter valido"
            break
        try:
            estado_nuevo = transiciones[(estado, caracter)]
        except KeyError:
            break
        print(f"|      {estado}      |    {caracter}    |     {caracter}     |      {estado_nuevo}       |")
        print("+--------------+---------+-----------+---------------+")
        estado = estado_nuevo
    if str(estado) == aceptar:
        print("""|                Cadena Valida :)                    |""")
        print("+--------------+---------+-----------+---------------+\n")
    else:
        print("""|              Cadena No Valida :(                   |""")
        print("+--------------+---------+-----------+---------------+\n")
        print(razon)

while True:
    print(f"""Seleccione una de las siguientes opciones:
    1. Automata ejercicio 2-a
    2. Automata ejercicio 2-b
    3. Automata ejercicio 2-c""")
    automata = input().replace(" ", "")
    if automata == "1":
        cadena = input("Ingrese una cadena para analizar:  ")
        caracteres = ["x", "y", "B"]
        transiciones = {("q1", "x"): "q2",  ("q2", "x"): "q2",  ("q2", "y"): "q2",  ("q2", "B"): "q3"}
        analisar(cadena, "q3")
        input("Presione enter para continuar")
    elif automata == "2":
        cadena = input("Ingrese una cadena para analizar:  ")
        caracteres = ["A", "C", "B"]
        transiciones = {("q1", "A"): "q2",  ("q1", "C"): "q1",  ("q1", "B"): "q3",  ("q2", "C"): "q1"}
        analisar(cadena, "q3")
        input("Presione enter para continuar")
    elif automata == "3":
        cadena = input("Ingrese una cadena para analizar:  ")
        caracteres = ["a", "b", "B"]
        transiciones = {("q1", "a"): "q5", ("q1", "b"): "q2", ("q2", "a"): "q5", ("q2", "b"): "q3",
                        ("q3", "a"): "q4", ("q3", "b"): "q3",  ("q4", "a"): "q5", ("q4", "b"): "q3",
                        ("q5", "a"): "q5", ("q5", "b"): "q3", ("q5", "B"): "q6"
                        }
        analisar(cadena, "q6")
        input("Presione enter para continuar")