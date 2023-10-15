from django.db import models

# Create your models here.


class Contact(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    profession = models.CharField(max_length = 200)
    telephone = models.IntegerField(max_length = 15)
    email = models.CharField(max_length= 200)
    picture = models.ImageField(upload_to='images/')
