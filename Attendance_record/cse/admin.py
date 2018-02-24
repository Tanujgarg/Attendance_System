from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Teachers)
admin.site.register(Student)
admin.site.register(WT)
admin.site.register(EIT)
admin.site.register(EITLab)
admin.site.register(WTLab)
admin.site.register(SE)
admin.site.register(SELab)
admin.site.register(BIE)
admin.site.register(MC)
admin.site.register(CD)
admin.site.register(Query)
admin.site.register(Auth)