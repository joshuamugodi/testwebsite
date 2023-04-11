from django.db import models

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length = 200)

    def __str__(self):
        return self.firstname
class Persons(models.Model):
    people = models.ForeignKey(Profile, on_delete= models.CASCADE)
    info = models.CharField(max_length= 500)
    complet = models.BooleanField()


    def __str__(self):
        return self.info

