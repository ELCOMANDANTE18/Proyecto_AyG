import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
import pandas as pd
import re
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Registro de Conexiones")
        self.df = None
        self.df_resultado = pd.DataFrame()
        self.setup_ui()

    def setup_ui(self):
        # Crear el botón para importar el archivo CSV
        importar_button = QPushButton("Importar CSV", self)
        importar_button.clicked.connect(self.importar_csv)

        # Crear la etiqueta para mostrar la ruta del archivo
        self.ruta_label = QLabel("", self)

        # Definir las variables para entrada de datos
        self.busqueda_entry = QLineEdit(self)
        self.fecha_inicio_entry = QLineEdit(self)
        self.fecha_fin_entry = QLineEdit(self)

        # Crear el botón para buscar
        buscar_button = QPushButton("Buscar", self)
        buscar_button.clicked.connect(self.buscar)

        # Crear el botón para exportar a Excel
        exportar_button = QPushButton("Exportar a Excel", self)
        exportar_button.clicked.connect(self.exportar_excel)

        # Crear la tabla para mostrar los resultados
        self.tabla_resultado = QTableWidget(self)

        # Crear el QLabel para mostrar mensajes de error y exportación exitosa
        self.mensaje_label = QLabel(self)

        # Configurar el diseño de la ventana principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(importar_button)
        layout.addWidget(self.ruta_label)
        layout.addWidget(QLabel("Búsqueda:"))
        layout.addWidget(self.busqueda_entry)
        layout.addWidget(QLabel("Fecha inicio:"))
        layout.addWidget(self.fecha_inicio_entry)
        layout.addWidget(QLabel("Fecha fin:"))
        layout.addWidget(self.fecha_fin_entry)
        layout.addWidget(buscar_button)
        layout.addWidget(exportar_button)
        layout.addWidget(self.tabla_resultado)
        layout.addWidget(self.mensaje_label)
        self.setCentralWidget(central_widget)

        # Establecer tamaño de la ventana
        self.resize(800, 600)

    def importar_csv(self):
        # Abrir el cuadro de diálogo para seleccionar el archivo
        archivo, _ = QFileDialog.getOpenFileName(self, "Importar archivo CSV", "", "Archivo CSV (*.csv)")

        if archivo:
            # Leer el archivo CSV y crear un DataFrame
            self.df = pd.read_csv(archivo)

            # Eliminar las filas que no tienen 16 valores
            self.df = self.df.dropna(thresh=16)

            # Obtener solo el nombre del archivo
            nombre_archivo = os.path.basename(archivo)

            # Actualizar la etiqueta de la ruta del archivo con el nombre
            self.ruta_label.setText(nombre_archivo)

    def buscar(self):
        if self.df is None or self.df.empty:  # Corregido: verificar si el DataFrame no está vacío
            self.mostrar_error("Error: No se ha importado ningún archivo CSV.")
            return

        # Obtener los valores de búsqueda y fecha
        busqueda = self.busqueda_entry.text()
        fecha_inicio = self.fecha_inicio_entry.text()
        fecha_fin = self.fecha_fin_entry.text()

        # Validar el formato de fecha
        fecha_regex = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(fecha_regex, fecha_inicio) or not re.match(fecha_regex, fecha_fin):
            self.mostrar_error("Error: El formato de fecha es inválido. Por favor ingrese una fecha en el formato AAAA-MM-DD.")
        else:
            # Expresión regular para el usuario
            usuario_regex = r'^[a-zA-Z0-9_-]+$'

            # Expresión regular para la fecha
            fecha_regex = r'^[0-9-]+$'

            # Expresión regular para la dirección MAC
            mac_regex = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

            # Filtrar las filas según las expresiones regulares
            df_filtrado = self.df[
                self.df['Usuario'].str.match(usuario_regex, na=False) &
                self.df['Inicio_de_Conexión_Dia'].str.match(fecha_regex, na=False) &
                self.df['FIN_de_Conexión_Dia'].str.match(fecha_regex, na=False) &
                self.df['MAC_Cliente'].str.match(mac_regex, na=False)
            ]

            # Filtrar las filas por búsqueda y fecha y asignarlas a un nuevo DataFrame
            df_filtrado = df_filtrado.loc[
                (df_filtrado['Usuario'].str.contains(busqueda, na=False)) &
                (df_filtrado['Inicio_de_Conexión_Dia'].between(fecha_inicio, fecha_fin))
            ]

            # Seleccionar las columnas relevantes y mostrar el resultado
            self.df_resultado = df_filtrado.loc[:, ['Usuario', 'Inicio_de_Conexión_Dia', 'FIN_de_Conexión_Dia', 'MAC_Cliente']]
            self.mostrar_resultado(self.df_resultado)

    def exportar_excel(self):
        if self.df_resultado.empty:
            self.mostrar_error("Error: No hay datos para exportar.")
            return

        # Abrir el cuadro de diálogo para seleccionar la ubicación del archivo
        archivo, _ = QFileDialog.getSaveFileName(self, "Exportar a Excel", "", "Archivo de Excel (*.xlsx)")

        if archivo:
            try:
                # Verificar si la extensión .xlsx ya está presente en el nombre del archivo
                _, extension = os.path.splitext(archivo)
                if extension.lower() != ".xlsx":
                    archivo += ".xlsx"

                # Establecer el motor como 'openpyxl' para escribir el archivo de Excel
                self.df_resultado.to_excel(archivo, index=False, engine='openpyxl')
                self.mostrar_mensaje("Exportación exitosa a Excel.")
            except Exception as e:
                self.mostrar_error(f"Error al exportar a Excel: {str(e)}")

    def mostrar_resultado(self, df):
        num_filas, num_columnas = df.shape

        # Configurar la tabla con el número de filas y columnas necesarias
        self.tabla_resultado.setRowCount(num_filas)
        self.tabla_resultado.setColumnCount(num_columnas)

        # Llenar la tabla con los datos del DataFrame
        for i, fila in enumerate(df.values):
            for j, dato in enumerate(fila):
                item = QTableWidgetItem(str(dato))
                self.tabla_resultado.setItem(i, j, item)

        self.mensaje_label.setText("")

    def mostrar_error(self, error):
        self.tabla_resultado.clearContents()  # Limpiar la tabla
        self.tabla_resultado.setRowCount(0)
        self.tabla_resultado.setColumnCount(0)
        self.mensaje_label.setText(error)

    def mostrar_mensaje(self, mensaje):
        self.tabla_resultado.clearContents()  # Limpiar la tabla
        self.tabla_resultado.setRowCount(0)
        self.tabla_resultado.setColumnCount(0)
        self.mensaje_label.setText(mensaje)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
