#!/bin/bash
# Entrar en el entorno virtual
cd .env
source bin/activate
cd ..
# Comprobar dependencias
pip3 install -r requirements.txt
# Ejecutar el programa
python3 main.py
