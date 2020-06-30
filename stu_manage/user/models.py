from django.db import models

class User(models.Model):
    name=models.CharField(max_length=64,verbose_name='学生名')
    password=models.CharField(max_length=32,verbose_name='用户密码')
    sex=models.CharField(max_length=2,verbose_name='用户性别')
    id=models.IntegerField(primary_key=True,blank=True,unique=True)
# Create your models here.
