from django.shortcuts import render
from django.http import JsonResponse
from Student.models import students,course
from user.models import User
import pymysql
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    else:
        data=request.POST
        User.objects.create(id=data['id'],name=data['name'],sex=data['sex'],password=data['password'])
        students.objects.create(id_id=data['id'],name=data['name'],sex=data['sex'],password=data['password'])
        return JsonResponse({'data':data})

#给前端传数据库数据

def getdata(request, course=course,students=students):

    user=list(User.objects.values())
    course=list(course.objects.values())
    student=list(students.objects.values())

    return JsonResponse({'data':user,'course':course,'students':student})


def getstudentdata(request,students=students):
    names=request.POST   #就收前端发来数据
    print(names)
    course_id = list(students.objects.filter(name=names['name']).values('stucourse')) # 学生所选课的id
    print(course_id)
    coursename=[]

    for i in range(len(course_id)):
        coursename +=list(course.objects.filter(cid=course_id[i]['stucourse']).values())

    return JsonResponse({'course':coursename})



def data_3(request,courses=course):
    deldata=request.POST
    print(deldata)
    print(deldata['courses[cid]'])
    ass=students.objects.get(name=deldata['name'])
    print(ass)
    course = courses.objects.get(cid=deldata['courses[cid]'])
    print(course)
    print(ass.stucourse.remove(course))    #删除对应学生表中的课程
    return JsonResponse('ok',safe=False)

def infodis(request):

    return render(request,'infodis.html')


#添加选课
def addcourse(request,courses=course):
    data=request.POST
    print(data)
    student=students.objects.get(id_id=data["stu_id"])
    print(student)
    course=courses.objects.get(cid=data['cid'])
    print(course)
    print(student.stucourse.add(course))     #添加未选课程
    #print(students.stucourse.get(cid=data['cid']))
    return JsonResponse('ok',safe=False)
