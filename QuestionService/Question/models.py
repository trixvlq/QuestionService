from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название вопроса')
    q_amount = models.PositiveIntegerField(default=1, verbose_name='Количество вопросов')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        abstract = True


class Question(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Option(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True



