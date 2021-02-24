from django.db import models

# Create your models here.


class Subscriber(models.Model):
    name = models.CharField("Name", max_length=100)
    age  = models.IntegerField("Age")
    email = models.EmailField("Email")

    def __str__(self):
        return self.name
