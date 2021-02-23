from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Search(models.Model):
    searchdomain = models.CharField(max_length=50)
    creation_date = models.DateTimeField(null=True)
    expiration_date = models.DateTimeField(null=True)
    availability = models.CharField(max_length=12, null=True)
    org = models.CharField(max_length=80, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    state = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.searchdomain