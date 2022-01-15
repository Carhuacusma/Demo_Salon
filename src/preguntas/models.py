from django.db import models

# Create your models here.
class Pregunta(models.Model):
    question = models.TextField()