from django.db import models
from user.models import User

class course(models.Model):
    cid=models.CharField(max_length=64,verbose_name='课程号',primary_key=True)
    name=models.CharField(max_length=128,verbose_name='课程名')



class students(models.Model):
    Course_ITEMS=[
        (0,'成功'),(1,'失败'),
    ]
    id=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=64,verbose_name='学生名')
    sex=models.CharField(verbose_name='性别',max_length=8)
    stu_status=models.IntegerField(choices=Course_ITEMS,verbose_name='选修课程状态',default=1)
    stucourse=models.ManyToManyField(course,verbose_name='选修的课程')
    password=models.CharField(max_length=32,blank=True)




# Create your models here.
