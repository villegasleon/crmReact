#install mysql on your computer
#pip install django
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python
# correr python mydb.py para que se genera la base de datos
#primera vez python manage.py makemigrations
# correr python manage.py migrate para que se creen todas las tablas predefinidas en mysql
# crear super user / python manage.py createsuperuser
#no olvidar revisar la configuracion de que base de datos esta guardanado:
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crmreactdb',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }"""
#ahora hacemos correr el servidor / python manage.py runserver


import mysql.connector

database= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'admin',
)

#prepare a cursor object
cursorObject= database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crmreactdb")

print('All Done!!')