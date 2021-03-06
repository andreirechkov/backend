from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


def upload_path(instance, filename):
    return '/'.join([filename])


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    email = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    link = ArrayField(models.CharField(max_length=50, blank=True), size=3, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    city = models.CharField(max_length=256, null=True)
    content = models.TextField(null=True)
    area = models.CharField(max_length=20, null=True)
    typeUser = models.CharField(max_length=256, null=True)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    nameNews = models.CharField(max_length=256, null=True)
    vacancy = models.TextField(null=True)
    workTime = models.TextField(null=True)
    experience = models.TextField(null=True)
    content = models.TextField(null=True)
    price = models.CharField(max_length=256, null=True)
    category = models.CharField(max_length=256, null=True)
    coordinate = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    image1 = models.ImageField(blank=True, null=True, upload_to=upload_path)
    image2 = models.ImageField(blank=True, null=True, upload_to=upload_path)
    image3 = models.ImageField(blank=True, null=True, upload_to=upload_path)
    image4 = models.ImageField(blank=True, null=True, upload_to=upload_path)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
