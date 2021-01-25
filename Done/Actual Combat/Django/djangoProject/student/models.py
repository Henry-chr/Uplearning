from django.db import models
import datetime

# Create your models here.
class pp_logon_user(models.Model):
    user_name  = models.CharField(max_length=50,unique=True)
    user_pwd   = models.CharField(max_length=50)

class pp_autologon_test(models.Model):
    user_name = models.CharField(max_length=100)
    user_id = models.IntegerField(max_length=15,unique=True)
    user_pwd = models.CharField(max_length=50)
    user_mail = models.EmailField(max_length=50)
    insert_time = models.TimeField(default=datetime.datetime.now())