from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='tests'),
    # path('quiz/<int:pk>/', quiz, name='home'),
]
