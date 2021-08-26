from django.db import models
from django.contrib.auth.models import User


# class Purchaser(models.Model):
#     pass


class Snack(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
