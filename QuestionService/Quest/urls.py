from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='quests'),
    # path('quiz/<int:pk>/', quiz, name='home'),
]
