from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=300)
    priority = models.IntegerField()
    date = models.DateField(default='2024-01-01')

    def __str__(self):
        return self.name