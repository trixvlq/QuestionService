from django.shortcuts import render

from Test.models import *


def index(request):
    tests = Test.objects.all()
    context = {
        'title':'Тесты',
        'tests':tests,
    }
    return render(request,'Question/special.html', context)