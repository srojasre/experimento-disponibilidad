
# Create your models here.
from django.db import models

class Admision(models.Model):
    paciente = models.CharField(max_length=100)
    razon = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente} - {self.razon}"
