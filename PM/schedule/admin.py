from django.contrib import admin
from .models import Profile, Employee,Work_day, Vacation, Free_days
# Register your models here.
admin.site.register(Profile)
admin.site.register(Employee)
admin.site.register(Work_day)
admin.site.register(Vacation)
admin.site.register(Free_days)