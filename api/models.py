from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    email = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=20, null=True)
    typeUser = models.CharField(max_length=256, null=True)


class Test(models.Model):
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Test"

    def __str__(self):
        return self.email
