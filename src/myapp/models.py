from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, default='Mulyono')
    password = models.CharField(max_length=128, default='thisispassword', blank=False)
    email = models.EmailField(unique=True, default="temp@gmail.com", blank=False)  
    
    GENDER_CHOICES = [ 
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.email  