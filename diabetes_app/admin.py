from django.contrib import admin
from .models import Diabetes_table
class ad(admin.ModelAdmin):
    list_display=('name','gender','age','blood_pressure','glucose','insulin','skin_thickness')
admin.site.register(Diabetes_table,ad)
# Register your models here.
