from django.db import models

# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name= models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    phone_number = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    date_of_birth = models.CharField(max_length=50,null=True,blank=True)
    skills = models.CharField(max_length=50,null=True,blank=True)
    story = models.TextField(null=True,blank=True)
    Volunteer_reason = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + self.last_name
