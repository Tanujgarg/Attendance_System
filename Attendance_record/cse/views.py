from django.shortcuts import render
from .forms import *
from .models import *
from .Files.Form_data import *

# Create your views here.


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
            user = Teachers.objects.filter(name=name).first()
            if user:
                if password == user.password:
                    request.session['name'] = user.name
                    return render(request, 'section.html',)
                else:
                    return render(request, 'teacherlogin.html', {'form': form,
                                                                 'error': 'Wrong Password'})
            else:
                return render(request, 'teacherlogin.html', {'form': form,
                                                             'error': 'No user exist with this name'})
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

            user = Student.objects.filter(roll_no=roll_no).first()

            if user:
                if user.password == password:
                    return render(request, '')
                else:
                    return render(request, 'studentlogin.html', {'form': form,
                                                                 'error': 'Wrong password'})
            else:
                return render(request, 'studentlogin.html', {'form': form,
                                                             'error': 'Incorrect roll number'})
        else:
            print("invalid")
    elif request.method == "GET":
        form = Teachers_login()
        return render(request, 'studentlogin.html', {'form': form})


def mark_attendance(request):
    if request.method == "GET":
        # print(request.session['name'])
        section = request.GET.get('class')
        print(section)
        if section == 'cse1':
            form = Cse1(request.POST)
            return render(request, 'attendance.html', {'form': form,
                                                       'data': Cse1_data})
        if section == 'cse1a':
            form = Cse1a(request.POST)
            return render(request, 'attendance.html', {'form': form,
                                                       'data': A1_data})
        elif section == 'cse1b':
            form = Cse1b(request.POST)
            return render(request, 'attendance.html', {'form': form,
                                                       'data': A2_data})
        elif section == 'cse1la':
            form = Cse1a(request.POST)
            return render(request, 'attendance.html', {'form': form,
                                                       'data': A1_data})
        elif section == 'cse1lb':
            form = Cse1b(request.POST)
            return render(request, 'attendance.html', {'form': form,
                                                       'students': A2_data})
    elif request.method == "POST":
        form = Cse1a(request.POST)
        print("Post")
        if form.is_valid():
            print("form valid")
            for i, j in zip(A1_roll, A_key):
                status = form.cleaned_data[j]
                print(status)
            return render(request, 'attendance.html')
