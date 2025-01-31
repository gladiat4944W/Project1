from django.db import models

class Order(models.Model):
    firstname = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    pizza_type = models.CharField(max_length=100)
    quantity = models.IntegerField()

    pizza_type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.firstname


# Create your models here.
