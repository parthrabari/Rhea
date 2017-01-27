from django.db import models

# Create your models here.
class LoginData(models.Model):
    """docstring for ."""
    reg_no    = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=50)
    phone_no  = models.IntegerField(max_length=10)
    email     = models.EmailField(max_length = 70)
    reg_type  = models.CharField(max_length=10)
    no_of_tkt = models.IntegerField(max_length=10)
