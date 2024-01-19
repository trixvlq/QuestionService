from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('test/', include('Test.urls')),
    path('quest/', include('Quest.urls')),
    path('survey/', include('Survey.urls')),
    path('quiz/<int:pk>/', quiz, name='home'),
]
