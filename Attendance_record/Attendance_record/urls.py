"""Attendance_record URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cse.views import *
# handler404 = 'cse.views.error'
# handler500 = 'cse.views.error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacherlogin', teachers_login),
    path('studentlogin', student_login),
    path('', index),
    path('attendance/', mark_attendance),
    path('home', index),
    path('studentsignup', student_register),
    # path('password', Change_password),
    path('dept', dept),
    path('feedback', feedback),
    path('authlogin', dept_login)
]
