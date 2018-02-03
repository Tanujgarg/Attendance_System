from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

cse1A = [6315003, 6315004, 6315005, 6315006, 6315009, 6315010, 6315011, 6315012, 6315013, 6315014, 6315015, 6315016,
         6315017, 6315018, 6315021, 6315023, 6315024, 6315025]

cse1B = [6315026, 6315027, 6315028, 6315029]


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
                    request.session['subject'] = user.subject
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
        section = request.GET.get('class')
        print(section)
        if section == 'cse1a':
            form = Cse1a(request.POST)
            return render(request, 'attendance.html', {'form': form,
                                                   'students': cse1A})
        elif section == 'cse1b':
            form = Cse1b(request.POST)
            return render(request, 'attendance.html', {'form': form,
                                                       'students': cse1B})

