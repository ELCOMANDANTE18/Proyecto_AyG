import pandas as pd

# Leer el archivo CSV y almacenar los datos en un DataFrame
df = pd.read_csv('Proyecto_AyG/Proyecto/Material/ByteNet.csv', low_memory=False)

# Seleccionar las columnas relevantes y asignarlas a un nuevo DataFrame
df_relevant = df.loc[:, ['Usuario', 'Inicio_de_Conexión_Dia', 'FIN_de_Conexión_Dia', 'MAC_Cliente']]

# Agregar una columna de ID utilizando la función reset_index()
df_relevant = df_relevant.reset_index()
df_relevant = df_relevant.rename(columns={'index': 'ID'})

# Exportar el DataFrame resultante a un archivo Excel utilizando la función to_excel()
df_relevant.to_excel('listado.xlsx', index=False)