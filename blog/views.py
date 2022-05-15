from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Employee


def home(request):
    employees = Employee.objects.all()
    return render(request, 'blog/home.html', {'employees': employees})
