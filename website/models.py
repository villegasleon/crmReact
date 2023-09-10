from django.db import models

# Crea una tabla para guardar los datos de clientes
class Record(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    addres = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

#Crear una tabla para almacenar los eventos de calendario
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_hour = models.TimeField(default='00:00')  
    end_hour = models.TimeField(default='00:00')  
    customer_record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    
    
