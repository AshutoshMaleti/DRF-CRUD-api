from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Tasks(models.Model):
    title=models.CharField(max_length=200)
    completed=BooleanField(default='False',blank='True',null='True')

    def __str__(self):
        return self.title