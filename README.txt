######################
# 1era configuración #
######################

1) Creación y configuración del entorno virtual:

Crear el entorno virtual: 
dentro de /OPUSLIST/, ejecutar: 'python -m venv .venv'

Activar el entorno virtual:
dentro de /OPUSLIST/, ejecutar: 'source .venv/bin/activate' -> (MAC/Linux)

Instalar dependencias:
dentro de /OPUSLIST/ con el entorno activado ejecutar: 'pip install -r requirements.txt'


2) Archivo .env

Crear un archivo llamado .env con los siguientes campos:

DB_USER -> su nombre de usuario en MySQL
DB_PASSWORD -> su contraseña en MySQL
DB_NAME -> un nombre de su elección para su base de datos

##########################
# Ejecución del programa #
##########################

1) Abrir servidor Uvicorn:

dentro de /OPUSLIST/ con el entorno activado ejecutar: 'uvicorn Backend.API.app:app --reload'

2) Iniciar el programa:

dentro de /OPUSLIST/ con el entorno activado ejecutar: 'python3 main.py'