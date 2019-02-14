from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')

# Register your models here.
admin.site.register(Job, JobAdmin)