from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)