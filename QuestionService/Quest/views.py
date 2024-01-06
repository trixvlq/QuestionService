from django.shortcuts import render

from Quest.models import *


def index(request):
    quests = Quest.objects.all()
    context = {
        'title': 'Квесты',
        'tests': quests,
    }
    return render(request, 'Question/special.html', context)
