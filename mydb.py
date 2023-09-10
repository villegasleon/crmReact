#install mysql on your computer
#pip install django
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python
# correr python mydb.py para que se genera la base de datos
# correr python manage.py migrate para que se creen todas las tablas predefinidas en mysql
# crear super user / python manage.py createsuperuser
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
cursorObject.execute("CREATE DATABASE crmdjangodb")

print('All Done!!')