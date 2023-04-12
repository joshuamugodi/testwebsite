from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length= 40, default = True)
    password = models.CharField(max_length= 100)


    def __str__(self):
        return self.firstname
class Persons(models.Model):
    info = models.CharField(max_length= 500)
    gender= models.BooleanField()


    def __str__(self):
        return self.info

