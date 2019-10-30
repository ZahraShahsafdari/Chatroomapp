from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    avatar = models.CharField(max_length = 50)
    active = models.BooleanField(default = True)

class Messages(models.Model):
    text = models.TextField()
    sender = models.IntegerField()
    receiver = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(default = 1) 
    #status : 1: sent 2: received 3. seen

