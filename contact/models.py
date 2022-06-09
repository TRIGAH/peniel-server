import email
from django.db import models

# Create your models here.
class Contact (models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name= models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    phone_number = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    discussion = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name + self.last_name

