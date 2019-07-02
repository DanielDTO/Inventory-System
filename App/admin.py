from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Desktop, Laptop, Mobile, Stationary)

#class Admin(admin.ModelAdmin):
class Admin(ImportExportModelAdmin):
    pass