from django.contrib import admin
from . models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'salary', 'gender']
    search_fields = ['name']
    list_per_page = 8
