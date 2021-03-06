from django.db import models
import os,datetime

# Create your models here.
class LoginData(models.Model):
    """docstring for ."""
    reg_no    = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=50)
    phone_no  = models.IntegerField()
    email     = models.EmailField(max_length = 70)
    id_card   = models.FileField(null=True,blank=True)
    reg_type  = models.CharField(max_length=10)
    no_of_tkt = models.IntegerField()
    reg_date  = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.title
