from django.db import models

# Create your models here.

class ProfileData(models.Model):
    name = models.CharField(max_length = 200,default = "ibrahim")
    profileFile = models.FileField(upload_to='news/',max_length=250,null=True,default=None)