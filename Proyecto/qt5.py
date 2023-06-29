import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget
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

        # Crear el widget de texto para mostrar el resultado
        self.resultado_text = QTextEdit(self)
        self.resultado_text.setReadOnly(True)

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
        layout.addWidget(self.resultado_text)
        self.setCentralWidget(central_widget)

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
        if self.df is not None and not self.df.empty:
            self.resultado_text.setPlainText("Error: No se ha importado ningún archivo CSV.")
            return

        # Obtener los valores de búsqueda y fecha
        busqueda = self.busqueda_entry.text()
        fecha_inicio = self.fecha_inicio_entry.text()
        fecha_fin = self.fecha_fin_entry.text()

        # Validar el formato de fecha
        fecha_regex = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(fecha_regex, fecha_inicio) or not re.match(fecha_regex, fecha_fin):
            self.resultado_text.setPlainText("Error: El formato de fecha es inválido. Por favor ingrese una fecha en el formato AAAA-MM-DD.")
        else:
            # Expresión regular para el usuario
            usuario_regex = r'^[a-zA-Z0-9_-]+$'

            # Expresión regular para la fecha
            fecha_regex = r'^[0-9-]+$'

            # Expresión regular para la dirección MAC
            mac_regex = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

            # Filtrar las filas según las expresiones regulares
            if self.df is None:
                self.resultado_text.setPlainText("Error: No se ha importado ningún archivo CSV.")
                return

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
            self.resultado_text.setPlainText(self.df_resultado.to_string(index=False))

    def exportar_excel(self):
        if self.df_resultado.empty:
            self.resultado_text.setPlainText("Error: No hay datos para exportar.")
            return

        # Abrir el cuadro de diálogo para seleccionar la ubicación del archivo
        archivo, _ = QFileDialog.getSaveFileName(self, "Exportar a Excel", "", "Archivo de Excel (*.xlsx)")

        if archivo:
            # Guardar el DataFrame en el archivo de Excel
            self.df_resultado.to_excel(archivo, index=False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
