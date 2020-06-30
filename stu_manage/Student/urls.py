from django.urls import path
from . import views
urlpatterns=[
    path('login/', views.login),
    path('reg/',views.register),
    path('getdata/',views.getdata),
    path('infodis/',views.infodis),
    path('getdatastudent/',views.getstudentdata),
    path('data_3/',views.data_3),
    path('addcourse/',views.addcourse)
]