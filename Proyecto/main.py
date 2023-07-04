import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QListWidget, QMessageBox
from PyQt5.QtGui import QPixmap
import qdarkstyle
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
        importar_button.setIcon(QtGui.QIcon("./icons/file-import.svg"))
        # Tamaño máximo del botón a tamaño del texto
        importar_button.setMaximumWidth(importar_button.sizeHint().width())

        # Crear la etiqueta para mostrar la ruta del archivo
        self.ruta_label = QLabel("", self)

        # Definir las variables para entrada de datos
        self.busqueda_entry = QLineEdit(self)
        self.fecha_inicio_entry = QLineEdit(self)
        self.fecha_fin_entry = QLineEdit(self)

        # Crear el botón para buscar
        buscar_button = QPushButton("Buscar", self)
        buscar_button.clicked.connect(self.buscar)
        buscar_button.setIcon(QtGui.QIcon("./icons/magnify.svg"))
        # Tamaño máximo del botón a tamaño del texto
        buscar_button.setMaximumWidth(buscar_button.sizeHint().width())

        # Crear el botón para exportar a Excel
        exportar_button = QPushButton("Exportar a Excel", self)
        exportar_button.clicked.connect(self.exportar_excel)
        exportar_button.setIcon(QtGui.QIcon("./icons/file-excel.svg"))
        # Tamaño máximo del botón a tamaño del texto
        exportar_button.setMaximumWidth(exportar_button.sizeHint().width())

        # Crear el widget de la tabla para mostrar el resultado
        self.tabla_resultado = QTableWidget(self)
        self.tabla_resultado.setColumnCount(4)
        self.tabla_resultado.setHorizontalHeaderLabels(["Usuario", "Fecha de conexión", "Fecha de desconexión", "Dirección MAC"])
        self.tabla_resultado.horizontalHeader().setStretchLastSection(True)
        self.tabla_resultado.resizeColumnsToContents()

        # Crear la etiqueta para mostrar mensajes
        self.mensaje_label = QLabel("", self)

        # Crear el widget de la lista de usuarios
        self.lista_usuarios = QListWidget(self)
        self.lista_usuarios.itemClicked.connect(self.copiar_usuario)

        # Crear botón "Acerca de"
        acerca_de_button = QPushButton("", self)
        acerca_de_button.clicked.connect(self.mostrar_acerca_de)
        # Establecer el tooltip
        acerca_de_button.setToolTip("Acerca de...")
        # SVG de la información
        acerca_de_button.setIcon(QtGui.QIcon("./icons/information.svg"))

        # Crear la zona de importación
        importar_layout = QHBoxLayout()
        importar_layout.addWidget(importar_button)
        importar_layout.addWidget(self.ruta_label)
        importar_layout.addWidget(acerca_de_button)
        # Tamaño máximo del botón "Acerca de"
        acerca_de_button.setMaximumWidth(24)

        # Crear la zona de búsqueda
        busqueda_layout = QHBoxLayout()
        busqueda_layout.addWidget(QLabel("Búsqueda:"))
        busqueda_layout.addWidget(self.busqueda_entry)

        # Crear la zona de fecha inicio
        fecha_inicio_layout = QHBoxLayout()
        fecha_inicio_layout.addWidget(QLabel("Fecha inicio:"))
        fecha_inicio_layout.addWidget(self.fecha_inicio_entry)

        # Crear la zona de fecha fin
        fecha_fin_layout = QHBoxLayout()
        fecha_fin_layout.addWidget(QLabel("Fecha fin:"))
        fecha_fin_layout.addWidget(self.fecha_fin_entry)

        # Crear la zona de botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(buscar_button)
        botones_layout.addWidget(exportar_button)

        # Crear la zona de mensajes
        mensaje_layout = QHBoxLayout()
        mensaje_layout.addWidget(self.mensaje_label)

        # Crear la zona de la lista de usuarios
        lista_usuarios_layout = QVBoxLayout()
        lista_usuarios_layout.addWidget(QLabel("Usuarios:"))
        lista_usuarios_layout.addWidget(self.lista_usuarios)
        
        # Hacer menos ancha la lista de usuarios
        self.lista_usuarios.setMaximumWidth(200)

        # Configurar el diseño de la ventana principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addLayout(importar_layout)
        layout.addLayout(busqueda_layout)
        layout.addLayout(fecha_inicio_layout)
        layout.addLayout(fecha_fin_layout)
        layout.addLayout(botones_layout)

        # Agregar la lista de usuarios y la tabla en un layout horizontal
        usuarios_tabla_layout = QHBoxLayout()
        usuarios_tabla_layout.addLayout(lista_usuarios_layout)
        usuarios_tabla_layout.addWidget(self.tabla_resultado)
        layout.addLayout(usuarios_tabla_layout)

        layout.addLayout(mensaje_layout)
        self.setCentralWidget(central_widget)

        # Establecer tema oscuro
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

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

            # Cargar los usuarios en la lista
            self.cargar_usuarios()

    def cargar_usuarios(self):
        if self.df is not None and not self.df.empty:
            usuarios = self.df['Usuario'].unique().tolist()
            usuarios = [usuario for usuario in usuarios if re.match(r'^[a-zA-Z0-9_-]+$', usuario)]
            usuarios.sort()  # Ordenar alfabéticamente
            self.lista_usuarios.clear()
            self.lista_usuarios.addItems(usuarios)
            self.lista_usuarios.adjustSize()

    def copiar_usuario(self, item):
        usuario = item.text()
        self.busqueda_entry.setText(usuario)

    def buscar(self):
        if self.df is None or self.df.empty:  # Verificar si el DataFrame no está vacío
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
            self.mostrar_tabla_resultado()

            # Borrar el mensaje de error
            self.mensaje_label.setText("")

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
                self.mostrar_mensaje("<span style='color: green'>Exportación exitosa a Excel.</span>")
            except Exception as e:
                self.mostrar_error(f"Error al exportar a Excel: {str(e)}")

    def mostrar_tabla_resultado(self):
        # Limpiar la tabla
        self.tabla_resultado.clearContents()
        self.tabla_resultado.setRowCount(0)

        # Establecer el número de filas y columnas
        num_filas = len(self.df_resultado)
        num_columnas = len(self.df_resultado.columns)

        # Establecer el número de filas y columnas en la tabla
        self.tabla_resultado.setRowCount(num_filas)
        self.tabla_resultado.setColumnCount(num_columnas)

        # Establecer los nombres de las columnas
        nombres_columnas = self.df_resultado.columns.tolist()
        self.tabla_resultado.setHorizontalHeaderLabels(["Usuario", "Inicio de Conexión", "Fin de Conexión", "MAC Cliente"])

        # Recorrer los datos del DataFrame y agregarlos a la tabla
        for i, fila in enumerate(self.df_resultado.itertuples(index=False), 0):
            for j, valor in enumerate(fila, 0):
                item = QTableWidgetItem(str(valor))
                self.tabla_resultado.setItem(i, j, item)

        # Ajustar el tamaño de las columnas al contenido
        self.tabla_resultado.resizeColumnsToContents()

        # Ajustar el ancho de la tabla a la ventana
        self.tabla_resultado.horizontalHeader().setStretchLastSection(True)

    def mostrar_mensaje(self, mensaje):
        self.mensaje_label.setText(mensaje)

    def mostrar_error(self, error):
        self.mensaje_label.setText(f"<span style='color: red'>{error}</span>")

    def mostrar_acerca_de(self):
        QMessageBox.about(self, "Acerca de", "<center>Este programa ha sido desarrollado por<br><a href='https://github.com/AdrianoTisera/'>Adriano Gabriel Tisera Aguilera</a><br><a href='https://github.com/ELCOMANDANTE18'>Víctor Benjamín Giménez</a><br><a href='https://github.com/perezmatias'>Matías Agustín Pérez</a><br><a href='https://github.com/facundomala1'>Facundo Gabriel Mala Palleres</a><br><a href='https://github.com/annapaez'>Anna Clara Páez Rocha</a><br><br>Para más información visite <a href='https://github.com/ELCOMANDANTE18/Proyecto_AyG'>el respositorio de Github</a></center>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
