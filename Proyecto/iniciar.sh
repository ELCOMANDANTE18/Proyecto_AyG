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
# Ejecutar el programa
python3 main.py
