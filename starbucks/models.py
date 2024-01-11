from django.db import models

# Create your models here.
class Coffee(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()

    def __str__(self):
        return self.name