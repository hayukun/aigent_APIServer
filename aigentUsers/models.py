from django.db import models

# Create your models here.
class Users(models.Model):

    displayName = models.CharField(max_length=200)
    userID = models.CharField(max_length=200)
