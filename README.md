# ospedale

# Requerimientos
Python 3.7.6 64bits

PostgreSQL

# Instrucciones
* Ejecute la consola de window `CMD`
* Crear en postgreSQL una base de datos llamada "ospedale"
###
    create database ospedale;
* Configurar los datos de conexión a la base de datos (name, user, y password) en la ruta `(ospedale/ospedale/settings/local.py)`
* Instalar python y agregarlo al path del sistema
* Instalar virtualevn
###
    pip install virtualenv
* Crear un nuevo entorno virtual de python por fuera de la ruta del proyecto `(../)`

Usando su version de python principal
###
    virtualenv venv-ospedale

O también puede utilizar un intérprete de Python de su elección
###
    virtualenv venv-ospedale -p c:\Python3\python.exe
* Active su entorno virtual
###
    venv-ospedale/Scripts/activate
* Regrese a la ruta principal del proyecto `(ospedale/)`
* Instale los requerimientos del sistema
###
    pip install -r requirements.txt
* Instale las migraciones
###
    python manage.py migrate
* Ejecute el servidor
###
    python manage.py runserver
