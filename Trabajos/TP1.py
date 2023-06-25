class AutomataNumero:
    def __init__(self):
        # Definir la matriz de transición
        self.matriz_transicion = {
            'q0': {'digit': 'q1', '.': 'q2', '+': 'q3', '-': 'q3'},
            'q1': {'digit': 'q1', '.': 'q4', 'e': 'q5', 'E': 'q5'},
            'q2': {'digit': 'q4'},
            'q3': {'digit': 'q1', '.': 'q2'},
            'q4': {'digit': 'q4', 'e': 'q5', 'E': 'q5'},
            'q5': {'digit': 'q7', '+': 'q6', '-': 'q6'},
            'q6': {'digit': 'q7'},
            'q7': {'digit': 'q7'}
        }


        # Definir el conjunto de estados de aceptación
        self.estados_aceptacion = {'q1', 'q2', 'q4', 'q7'}


    def reconocer_numero(self, cadena):
        estado_actual = 'q0'
        for simbolo in cadena:
            if simbolo.isdigit():
                simbolo = 'digit'
            if simbolo not in self.matriz_transicion[estado_actual]:
                return False
            estado_actual = self.matriz_transicion[estado_actual][simbolo]
        return estado_actual in self.estados_aceptacion


# Crear una instancia de AutomataNumero
automata = AutomataNumero()


# Solicitar al usuario que ingrese una cadena
cadena = input("Ingrese una cadena para verificar si es un número válido: ")


# Verificar si la cadena es un número válido
if automata.reconocer_numero(cadena):
    print(f"La cadena {cadena} es un número válido")
else:
    print(f"La cadena {cadena} no es un número válido")

