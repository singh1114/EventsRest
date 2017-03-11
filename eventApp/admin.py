from django.contrib import admin

from .models import EventList, MemberList, ParticipantsList
# Register your models here.

admin.site.register(EventList)
admin.site.register(MemberList)
admin.site.register(ParticipantsList)
