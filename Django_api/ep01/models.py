from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 40)
    roll = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.name) +" | "+ str(self.id) +" | "+ str(self.city)