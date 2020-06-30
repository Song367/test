from django.contrib import admin
from user.models import User
from Student.models import students,course

admin.site.register(User)
admin.site.register(students)
admin.site.register(course)
# Register your models here.
