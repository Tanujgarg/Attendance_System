from django.db import models

# Create your models here.


class Teachers(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Student(models.Model):
    roll_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Query(models.Model):
    roll_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()


class WT(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class EIT(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class CD(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class BIE(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class SE(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class MC(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class WTLab(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class EITLab(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class SELab(models.Model):
    roll_no = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
