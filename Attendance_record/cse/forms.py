from django import forms


class Teachers_login(forms.Form):
    name = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class Student_login(forms.Form):
    roll_no = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class Student_Signup(forms.Form):
    name = forms.CharField(max_length=255)
    roll_no = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class Cse1a(forms.Form):
    Student1 = forms.BooleanField(initial=False, required=False)
    Student2 = forms.BooleanField(initial=False, required=False)
    Student3 = forms.BooleanField(initial=False, required=False)
    Student4 = forms.BooleanField(initial=False, required=False)
    Student5 = forms.BooleanField(initial=False, required=False)
    Student6 = forms.BooleanField(initial=False, required=False)
    Student7 = forms.BooleanField(initial=False, required=False)
    Student8 = forms.BooleanField(initial=False, required=False)
    Student9 = forms.BooleanField(initial=False, required=False)
    Student10 = forms.BooleanField(initial=False, required=False)
    Student11 = forms.BooleanField(initial=False, required=False)
    Student12 = forms.BooleanField(initial=False, required=False)
    Student13 = forms.BooleanField(initial=False, required=False)
    Student14 = forms.BooleanField(initial=False, required=False)
    Student15 = forms.BooleanField(initial=False, required=False)
    Student16 = forms.BooleanField(initial=False, required=False)
    Student17 = forms.BooleanField(initial=False, required=False)
    Student18 = forms.BooleanField(initial=False, required=False)
    student19 = forms.BooleanField(initial=False, required=False)


class Cse1b(forms.Form):
    Student1 = forms.BooleanField(initial=False, required=False)
    Student2 = forms.BooleanField(initial=False, required=False)
    Student3 = forms.BooleanField(initial=False, required=False)
    Student4 = forms.BooleanField(initial=False, required=False)
    Student5 = forms.BooleanField(initial=False, required=False)
    Student6 = forms.BooleanField(initial=False, required=False)
    Student7 = forms.BooleanField(initial=False, required=False)
    Student8 = forms.BooleanField(initial=False, required=False)
    Student9 = forms.BooleanField(initial=False, required=False)
    Student10 = forms.BooleanField(initial=False, required=False)
    Student11 = forms.BooleanField(initial=False, required=False)
    Student12 = forms.BooleanField(initial=False, required=False)
    Student13 = forms.BooleanField(initial=False, required=False)
    Student14 = forms.BooleanField(initial=False, required=False)
    Student15 = forms.BooleanField(initial=False, required=False)
    Student16 = forms.BooleanField(initial=False, required=False)
    Student17 = forms.BooleanField(initial=False, required=False)
    Student18 = forms.BooleanField(initial=False, required=False)


class Cse1(forms.Form):
    Student1 = forms.BooleanField(initial=False, required=False)
    Student2 = forms.BooleanField(initial=False, required=False)
    Student3 = forms.BooleanField(initial=False, required=False)
    Student4 = forms.BooleanField(initial=False, required=False)
    Student5 = forms.BooleanField(initial=False, required=False)
    Student6 = forms.BooleanField(initial=False, required=False)
    Student7 = forms.BooleanField(initial=False, required=False)
    Student8 = forms.BooleanField(initial=False, required=False)
    Student9 = forms.BooleanField(initial=False, required=False)
    Student10 = forms.BooleanField(initial=False, required=False)
    Student11 = forms.BooleanField(initial=False, required=False)
    Student12 = forms.BooleanField(initial=False, required=False)
    Student13 = forms.BooleanField(initial=False, required=False)
    Student14 = forms.BooleanField(initial=False, required=False)
    Student15 = forms.BooleanField(initial=False, required=False)
    Student16 = forms.BooleanField(initial=False, required=False)
    Student17 = forms.BooleanField(initial=False, required=False)
    Student18 = forms.BooleanField(initial=False, required=False)
    Student19 = forms.BooleanField(initial=False, required=False)
    Student20 = forms.BooleanField(initial=False, required=False)
    Student21 = forms.BooleanField(initial=False, required=False)
    Student22 = forms.BooleanField(initial=False, required=False)
    Student23 = forms.BooleanField(initial=False, required=False)
    Student24 = forms.BooleanField(initial=False, required=False)
    Student25 = forms.BooleanField(initial=False, required=False)
    Student26 = forms.BooleanField(initial=False, required=False)
    Student27 = forms.BooleanField(initial=False, required=False)
    Student28 = forms.BooleanField(initial=False, required=False)
    Student29 = forms.BooleanField(initial=False, required=False)
    Student30 = forms.BooleanField(initial=False, required=False)
    Student31 = forms.BooleanField(initial=False, required=False)
    Student32 = forms.BooleanField(initial=False, required=False)
    Student33 = forms.BooleanField(initial=False, required=False)
    Student34 = forms.BooleanField(initial=False, required=False)
    Student35 = forms.BooleanField(initial=False, required=False)
    Student36 = forms.BooleanField(initial=False, required=False)


class Feedback_Form(forms.Form):
    name = forms.CharField(max_length=25)
    roll_no = forms.CharField(max_length=20, required=False, initial=None)
    email = forms.CharField(max_length=50)
    message = forms.CharField(max_length=1000)


class Change_password(forms.Form):
    name = forms.CharField(max_length=25)
    old = forms.CharField(max_length=25)
    new = forms.CharField(max_length=25)

class modify(forms.Form):
    roll_no = forms.CharField(max_length=10)
    is_lab = forms.BooleanField(required=False, initial=False)