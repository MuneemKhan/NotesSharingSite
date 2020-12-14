from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,null=True)
    department = models.CharField(max_length=30)
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadDate = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.signup.user.username+" "+self.status