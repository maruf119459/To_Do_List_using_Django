from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    title =  models.CharField(primary_key=True,max_length=30)
    description = models.TextField()