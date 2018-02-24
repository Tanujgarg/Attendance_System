from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from .Files.Form_data import *
import datetime
from cse.Files.Library.Data.Database import *

form_class = None
subject = ''
is_lab = False


def index(request):
    return render(request, 'index.html')


def teachers_login(request):
    global subject
    if request.method == 'POST':
        form = Teachers_login(request.POST)
        if form.is_valid():
            print("Form valid")
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print(name, password)
            user = Teachers.objects.filter(name=name.lower()).first()
            if user:
                if password == user.password:
                    request.session['name'] = user.name
                    request.session['subject'] = user.subject
                    subject = user.subject
                    return render(request, 'section.html',)
                else:
                    return render(request, 'teacherlogin.html', {'form': form,
                                                                 'error': 'Wrong Password'})
            else:
                return render(request, 'teacherlogin.html', {'form': form,
                                                             'error': 'No user exist with this name'})
            # print(name, password)
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
                    wt = WT.objects.filter(roll_no=roll_no).all()
                    cd = CD.objects.filter(roll_no=roll_no).all()
                    mc = MC.objects.filter(roll_no=roll_no).all()
                    eit = EIT.objects.filter(roll_no=roll_no).all()
                    eit_lab = EITLab.objects.filter(roll_no=roll_no).all()
                    se = SE.objects.filter(roll_no=roll_no).all()
                    se_lab = SELab.objects.filter(roll_no=roll_no).all()
                    bie = BIE.objects.filter(roll_no=roll_no).all()
                    wt_lab = WTLab.objects.filter(roll_no=roll_no).all()

                    wt_total = wt.count()
                    wt_present = wt.filter(status=True).count()
                    try:
                        wt_avg = (wt_present / wt_total) * 100
                        wt_avg = round(wt_avg, 2)
                    except ZeroDivisionError:
                        wt_avg = 'N.A.'

                    cd_total = cd.count()
                    cd_present = cd.filter(status=True).count()
                    try:
                        cd_avg = (cd_present / cd_total) * 100
                        cd_avg = round(cd_avg, 2)
                    except ZeroDivisionError:
                        cd_avg = 'N.A.'

                    mc_total = mc.count()
                    mc_present = mc.filter(status=True).count()
                    try:
                        mc_avg = (mc_present / mc_total) * 100
                        mc_avg = round(mc_avg, 2)
                    except ZeroDivisionError:
                        mc_avg = 'N.A.'

                    eit_total = eit.count()
                    eit_present = eit.filter(status=True).count()
                    try:
                        eit_avg = (eit_present / eit_total) * 100
                        eit_avg = round(eit_avg, 2)
                    except ZeroDivisionError:
                        eit_avg = 'N.A.'

                    se_total = se.count()
                    se_present = se.filter(status=True).count()
                    try:
                        se_avg = (se_present / se_total) * 100
                        se_avg = round(se_avg, 2)
                    except ZeroDivisionError:
                        se_avg = 'N.A.'

                    bie_total = bie.count()
                    bie_present = bie.filter(status=True).count()
                    try:
                        bie_avg = (bie_present / wt_total) * 100
                        bie_avg = round(bie_avg, 2)
                    except ZeroDivisionError:
                        bie_avg = 'N.A.'

                    wt_lab_total = wt_lab.count()
                    wt_lab_present = wt_lab.filter(status=True).count()
                    try:
                        wt_lab_avg = (wt_lab_present / wt_lab_total) * 100
                        wt_lab_avg = round(wt_lab_avg, 2)
                    except ZeroDivisionError:
                        wt_lab_avg = 'N.A.'

                    se_lab_total = se_lab.count()
                    se_lab_present = se_lab.filter(status=True).count()
                    try:
                        se_lab_avg = (se_lab_present / se_lab_total) * 100
                        se_lab_avg = round(se_lab_avg, 2)
                    except ZeroDivisionError:
                        se_lab_avg = 'N.A.'

                    eit_lab_total = eit_lab.count()
                    eit_lab_present = eit_lab.filter(status=True).count()
                    try:
                        eit_lab_avg = (eit_lab_present / eit_lab_total) * 100
                        eit_lab_avg = round(eit_lab_avg, 2)
                    except ZeroDivisionError:
                        eit_lab_avg = 'N.A.'

                    return render(request, 'Dashboard.html', {'wt': wt,
                                                              'user': user,
                                                              'cd': cd,
                                                              'mc': mc,
                                                              'eit': eit,
                                                              'eit_lab': eit_lab,
                                                              'se': se,
                                                              'se_lab': se_lab,
                                                              'bie': bie,
                                                              'wt_lab': wt_lab,
                                                              'wt_total': wt_total,
                                                              'wt_present': wt_present,
                                                              'wt_avg': wt_avg,
                                                              'se_total': se_total,
                                                              'se_present': se_present,
                                                              'se_avg': se_avg,
                                                              'eit_total': eit_total,
                                                              'eit_present': eit_present,
                                                              'eit_avg': eit_avg,
                                                              'mc_total': mc_total,
                                                              'mc_present': mc_present,
                                                              'mc_avg': mc_avg,
                                                              'cd_total': cd_total,
                                                              'cd_present': cd_present,
                                                              'cd_avg': cd_avg,
                                                              'bie_total': bie_total,
                                                              'bie_present': bie_present,
                                                              'bie_avg': bie_avg,
                                                              'wt_lab_total': wt_lab_total,
                                                              'wt_lab_present': wt_lab_present,
                                                              'wt_lab_avg': wt_lab_avg,
                                                              'se_lab_total': se_lab_total,
                                                              'se_lab_present': se_lab_present,
                                                              'se_lab_avg': se_lab_avg,
                                                              'eit_lab_total': eit_lab_total,
                                                              'eit_lab_present': eit_lab_present,
                                                              'eit_lab_avg': eit_lab_avg})
                else:
                    return render(request, 'studentlogin.html', {'form': form,
                                                                 'error': 'Wrong password'})
            else:
                return render(request, 'studentlogin.html', {'form': form,
                                                             'error': 'Incorrect roll number'})
        else:
            print("invalid")
    elif request.method == "GET":
        form = Student_login()
        return render(request, 'studentlogin.html', {'form': form})


def mark_attendance(request):
    global form_class
    global is_lab
    if request.method == "GET":
        if request.session.has_key('name'):
            print(request.session['name'])
            section = request.GET.get('class')
            # print(section, request.GET.get('key'))
            if section == 'cse1':
                form_class = 'cse1'
                print(section, form_class)
                form = Cse1(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': Cse1_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            if section == 'cse1a':

                form_class = 'cse1a'
                form = Cse1a(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A1_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            elif section == 'cse1b':

                form_class = 'cse1b'
                form = Cse1b(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A2_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            elif section == 'cse1la':
                is_lab = True
                form_class = 'cse1la'
                form = Cse1a(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A1_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            elif section == 'cse1lb':
                is_lab = True
                form_class = 'cse1lb'
                form = Cse1b(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A2_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})

            else:
                return redirect("/home")
        return render(request, 'Error.html', {'login_error': True})
    elif request.method == "POST":
        if form_class == 'cse1':
            form = Cse1(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                print(form_class)
                for i, j in zip(Cse1_roll, Cse1_key):
                    status = form.cleaned_data[j]
                    print(i, status)
                    if subject == 'wt' and not is_lab:
                        attendance = WT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and not is_lab:
                        attendance = EIT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'bie':
                        attendance = BIE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and not is_lab:
                        attendance = SE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'mc':
                        attendance = MC(roll_no=i, status=status)
                        attendance.save()
                        print("mc saved")
                    elif subject == 'cd':
                        attendance = CD(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'error': True})
                    # print(i, status)
        if form_class == 'cse1a':
            form = Cse1a(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A1_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and not is_lab:
                        attendance = WT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and not is_lab:
                        attendance = EIT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'bie':
                        attendance = BIE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and not is_lab:
                        attendance = SE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'mc':
                        attendance = MC(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'cd':
                        attendance = CD(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'error': True})
        if form_class == 'cse1b':
            form = Cse1b(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A2_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and not is_lab:
                        attendance = WT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and not is_lab:
                        attendance = EIT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'bie':
                        attendance = BIE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and not is_lab:
                        attendance = SE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'mc':
                        attendance = MC(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'cd':
                        attendance = CD(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'error': True})
        if form_class == 'cse1la':
            form = Cse1a(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A1_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and is_lab:
                        attendance = WTLab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and is_lab:
                        attendance = SELab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and is_lab:
                        attendance = EITLab(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'lab_error': True})
        if form_class == 'cse1lb':
            form = Cse1b(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A2_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and is_lab:
                        attendance = WTLab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and is_lab:
                        attendance = SELab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and is_lab:
                        attendance = EITLab(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'lab_error': True})
        request.session.flush()
        return render(request, 'Error.html', {'success': True})


def student_register(request):
    if request.method == "POST":
        print("Post")
        form = Student_Signup(request.POST)
        if form.is_valid():
            print("valid")
            name = form.cleaned_data['name']
            roll_no = form.cleaned_data['roll_no']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(name, password, email, roll_no)
            student = Student(name=name, roll_no=roll_no, email=email, password=password)
            student.save()
            print("saved")
            return render(request, 'Error.html', {'signup': True})
    elif request.method == "GET":
        print("Get")
        # return render(request, 'Signup.html')
    return render(request, 'Signup.html')


def Change_password(request):
    if request.method == "GET":
        teacher = request.GET.get('name')
        password = request.GET.get('pswrd')
        print(teacher, password)
        user = Teachers.objects.filter(name=teacher).first()
        user.password = password

        user.save()
        print("saved")
        print(user.password)
    return HttpResponse("Password Changed")


def dept(request):
    if request.method == "GET":
        if request.session.has_key('dept'):
            request.session.flush()
            wt = []
            se = []
            mc = []
            cd = []
            bie = []
            eit = []
            wt_lab = []
            se_lab = []
            eit_lab = []
            wt_avg = []
            se_avg = []
            mc_avg = []
            cd_avg = []
            bie_avg = []
            eit_avg = []
            wt_lab_avg = []
            se_lab_avg = []
            eit_lab_avg = []
            for i in Cse1_roll:
                obj = DataByRollNo(i)
                wt.append(obj.wt_present)
                se.append(obj.se_present)
                mc.append(obj.mc_present)
                cd.append(obj.cd_present)
                bie.append(obj.bie_present)
                eit.append(obj.eit_present)
                wt_lab.append(obj.wt_lab_present)
                se_lab.append(obj.se_lab_present)
                eit_lab.append(obj.eit_lab_present)
                wt_avg.append(obj.wt_avg)
                se_avg.append(obj.se_avg)
                mc_avg.append(obj.mc_avg)
                cd_avg.append(obj.cd_avg)
                bie_avg.append(obj.bie_avg)
                eit_avg.append(obj.eit_avg)
                wt_lab_avg.append(obj.wt_lab_avg)
                se_lab_avg.append(obj.se_lab_avg)
                eit_lab_avg.append(obj.eit_lab_avg)
                # print(wt)
            data = list(
                zip(Cse1_roll, wt, wt_avg, se, se_avg, mc, mc_avg, bie, bie_avg, eit, eit_avg, cd, cd_avg, wt_lab,
                    wt_lab_avg,
                    se_lab, se_lab_avg, eit_lab, eit_lab_avg))
            return render(request, 'Students_attendance_data.html', {'data': data,
                                                                     'wt_total': wt_total,
                                                                     'wt_req': wt_req,
                                                                     'wt_lab_total': wt_lab_total,
                                                                     'wt_lab_req': wt_lab_req,
                                                                     'se_total': se_total,
                                                                     'se_req': se_req,
                                                                     'se_lab_total': se_lab_total,
                                                                     'se_lab_req': se_lab_req,
                                                                     'eit_total': eit_total,
                                                                     'eit_req': eit_req,
                                                                     'eit_lab_total': eit_lab_total,
                                                                     'eit_lab_req': eit_lab_req,
                                                                     'cd_total': cd_total,
                                                                     'cd_req': cd_req,
                                                                     'mc_total': mc_total,
                                                                     'mc_req': mc_req,
                                                                     'bie_total': bie_total,
                                                                     'bie_req': bie_req})
        return render(request, 'Error.html', {'login_error': True})
    else:
        return HttpResponse("Bad Request")


def dept_login(request):
    if request.method == "POST":
        form = Teachers_login(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print(name,password)

            user = Auth.objects.filter(name=name.lower()).first()
            if user:
                if user.password == password:
                    request.session['dept'] = name
                    return redirect('/dept')
                else:
                    return render(request, 'authlogin.html', {'error': 'Incorrect password'})
            else:
                return render(request, 'authlogin.html', {'error': 'User not found'})
    elif request.method == "GET":
        return render(request, 'authlogin.html', {})


def feedback(request):
    if request.method == "POST":
        form = Feedback_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll_no = form.cleaned_data['roll_no']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(message)
            feed = Query(name=name, roll_no=roll_no, email=email, message=message)
            try:
                feed.save()
            except:
                return render(request, 'Error.html', {'error': True})
            print('saved')
            return render(request, 'Error.html', {'feed': True})
    elif request.method == "GET":
        return render(request, 'Feedback.html', {})
