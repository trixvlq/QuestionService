from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    tests = Test.objects.all()
    context = {
        'tests': tests
    }
    return render(request, 'Question/index.html', context=context)


# def quiz(request, pk):
