from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(models.Branch)
# admin.site.register(models.Appointment)
# admin.site.register(models.Bill)
# admin.site.register(models.Lab)
admin.site.register(models.Customer)
# admin.site.register(models.Report)
# admin.site.register(models.Review)
admin.site.register(models.Staff)
# admin.site.register(models.Test)
admin.site.register(models.User,UserAdmin)