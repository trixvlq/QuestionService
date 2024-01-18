from django.shortcuts import render

from Survey.models import *


def index(request):
    surveys = Survey.objects.all()
    context = {
        'title':'Опросы',
        'tests':surveys,
    }
    return render(request,'Question/special.html', context)