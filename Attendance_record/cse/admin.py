from django.contrib import admin
from django.contrib.sessions.models import Session
import pprint
# Register your models here.
from .models import *


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags=True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']


admin.site.register(Session, SessionAdmin)
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
# admin.site.register(Session)