from django.http import HttpResponse
from django.shortcuts import render

from Quest.models import Quest
from Survey.models import Survey
from Test.models import Test
from .models import *


def index(request):
    tests = Test.objects.all()
    surveys = Survey.objects.all()
    quests = Quest.objects.all()
    context = {
        'tests': tests,
        'surveys': surveys,
        'quests': quests,
    }
    return render(request, 'Question/index.html', context=context)


def quiz(request, pk):
    return render(request,'Question/test.html')