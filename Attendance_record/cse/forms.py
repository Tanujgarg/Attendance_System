from django import forms

class Teachers_login(forms.Form):
    name = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class Student_login(forms.Form):
    roll_no = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    status = forms.BooleanField(initial=False, required=False)


