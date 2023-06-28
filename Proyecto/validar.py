import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import re

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Conexiones")

# Leer el archivo CSV y crear un DataFrame
df = pd.read_csv("~/Coding/Facultad/Proyecto_AyG/Proyecto/Material/ByteNet.csv")

# Eliminar las filas que no tienen 16 valores
df = df.dropna(thresh=16)

# Definir las variables para entrada de datos
busqueda_entry = ttk.Entry(root)
busqueda_entry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)
fecha_inicio_entry = ttk.Entry(root)
fecha_inicio_entry.grid(column=2, row=1, padx=5, pady=5, sticky=tk.W)
fecha_fin_entry = ttk.Entry(root)
fecha_fin_entry.grid(column=3, row=1, padx=5, pady=5, sticky=tk.W)

# Definir la variable df_resultado
df_resultado = pd.DataFrame()

# Crear una función para buscar en el DataFrame
def buscar():
    # Obtener los valores de búsqueda y fecha
    busqueda = busqueda_entry.get()
    fecha_inicio = fecha_inicio_entry.get()
    fecha_fin = fecha_fin_entry.get()

    # Validar el formato de fecha
    fecha_regex = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(fecha_regex, fecha_inicio) or not re.match(fecha_regex, fecha_fin):
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Error: El formato de fecha es inválido. Por favor ingrese una fecha en el formato AAAA-MM-DD.")
    else:
        # Filtrar las filas por búsqueda y fecha y asignarlas a un nuevo DataFrame
        df_filtrado = df.loc[(df['Usuario'].str.contains(busqueda, na=False)) & (df['Inicio_de_Conexión_Dia'].between(fecha_inicio, fecha_fin))]

        # Seleccionar las columnas relevantes y mostrar el resultado
        global df_resultado
        df_resultado = df_filtrado.loc[:, ['Usuario', 'Inicio_de_Conexión_Dia', 'FIN_de_Conexión_Dia', 'MAC_Cliente']]
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, df_resultado.to_string(index=False))

buscar_button = ttk.Button(root, text="Buscar", command=buscar)
buscar_button.grid(column=4, row=1, padx=5, pady=5, sticky=tk.W)

# Crear un cuadro de texto scrolleable para mostrar los resultados
resultado_label = ttk.Label(root, text="Resultados:")
resultado_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
resultado_text = tk.Text(root, height=10, width=80)
resultado_text.grid(column=0, row=3, columnspan=5, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
resultado_scroll = ttk.Scrollbar(root, command=resultado_text.yview)
resultado_scroll.grid(column=5, row=3, padx=5, pady=5, sticky=tk.N+tk.S)
resultado_text.config(yscrollcommand=resultado_scroll.set)

# Crear un botón de exportación
def exportar():
    # Exportar el DataFrame resultante a un archivo Excel utilizando la función to_excel()
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Workbook", "*.xlsx")])
    if nombre_archivo:
        global df_resultado
        df_resultado.to_excel(nombre_archivo, index=False)

exportar_button = ttk.Button(root, text="Exportar a Excel", command=exportar)
exportar_button.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

# Ejecutar la ventana principal
root.mainloop()
