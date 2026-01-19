from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class PersonalModel(models.Model):

    user = models.ForeignKey(User,on_delete= models.CASCADE)

    title = models.CharField(max_length=10)

    content = models.CharField(max_length=30)

    created_at = models.DateField(auto_now_add= True)
