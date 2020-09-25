from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=120,)
    last_name = models.CharField(max_length=120)
    email_address = models.EmailField(max_length = 254) 
    phone = models.BigIntegerField() 
 
    def __str__(self):
        return self.first_name