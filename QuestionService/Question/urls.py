from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('quiz/<int:pk>/', quiz, name='home'),
]
