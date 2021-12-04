from django.db import models

# Create your models here.
class Estudiante(models.Model):
    username = models.TextField()
    email = models.EmailField(default='prueba@example.com')