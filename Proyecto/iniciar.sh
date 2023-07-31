#!/bin/bash
# Crear directorio para el entorno virtual
mkdir .env
# Crear entorno virtual
python3 -m venv .env
# Entrar en el entorno virtual
cd .env
source bin/activate
cd ..
# Comprobar dependencias
pip3 install -r requirements.txt

# Preguntar si se quiere extraer la base de datos de ejemplo
echo "¿Desea extraer la base de datos de ejemplo? (s/n)"
read respuesta
if [ $respuesta = "s" ]; then
    # Extraer base de datos de ejemplo
    unzip -o Material/example.zip
fi

# Ejecutar el programa
python3 main.py
