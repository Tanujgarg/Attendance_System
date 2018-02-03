from django import forms

class Teachers_login(forms.Form):
    name = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class Student_login(forms.Form):
    roll_no = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class Cse1a(forms.Form):
    student = forms.BooleanField(initial=False, required=False)
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


class Cse1b(forms.Form):
    student = forms.BooleanField(initial=False, required=False)
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