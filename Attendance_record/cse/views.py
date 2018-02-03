from django.shortcuts import render
from .forms import *
from .models import models

# Create your views here.

cse1A = [6315003, 6315004, 6315005, 6315006, 6315009, 6315010, 6315011, 6315012, 6315013, 6315014, 6315015, 6315016,
         6315017, 6315018, 6315021, 6315023, 6315024, 6315025]


def index(request):
    return render(request, 'index.html')


def teachers_login(request):
    if request.method == 'POST':
        form = Teachers_login(request.POST)
        if form.is_valid():
            print("Form valid")
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print(name, password)
        else:
            print("invalid")
    elif request.method == "GET":
        form = Teachers_login()
    return render(request, 'teacherlogin.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = Student_login(request.POST)
        if form.is_valid():
            print("Form valid")
            roll_no = form.cleaned_data['roll_no']
            password = form.cleaned_data['password']
            status = form.cleaned_data['status']
            print(roll_no, password, status)
        else:
            print("invalid")
    elif request.method == "GET":
        form = Teachers_login()
    return render(request, 'studentlogin.html', {'form': form,})
