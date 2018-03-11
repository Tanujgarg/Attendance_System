from django.db import models

# Create your models here.


class Teachers(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, default=None)
    roll_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.roll_no


class Query(models.Model):
    name = models.CharField(max_length=255, default=None)
    roll_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class WT(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class EIT(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class CD(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class BIE(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class SE(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class MC(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class WTLab(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class EITLab(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class SELab(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no + '_' + str(self.date)


class Auth(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name