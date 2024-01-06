from django.contrib.auth.models import User
from django.db import models
from Question.models import Quiz, Question, Option


class Quest(Quiz):
    question_amount = models.IntegerField(default=0, verbose_name='Количество вопросов')

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'


class QuestResult(models.Model):
    min_score = models.IntegerField(verbose_name='Минимальный порог')
    max_score = models.IntegerField(verbose_name='Максимальный порог')
    text = models.TextField(verbose_name='Текст с концовкой')
    img = models.ImageField(upload_to='static/images/%Y/%m/%d/', blank=True, verbose_name='Картинка в конце')

    class Meta:
        verbose_name = 'Конецовка теста'
        verbose_name_plural = 'Концовки тестов'


class QuestionQuest(Question):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, verbose_name='Опрос')

    class Meta:
        verbose_name = 'Вопрос квеста'
        verbose_name_plural = 'Вопросы квеста'


class OptionQuest(Option):
    quest = models.ForeignKey(QuestionQuest, on_delete=models.CASCADE, verbose_name='Опрос')
    power = models.IntegerField(default=0, verbose_name='Значение опции')

    class Meta:
        verbose_name = 'Вариант ответа квеста'
        verbose_name_plural = 'Варианты ответов квестов'


class QuestAttempt(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    contender = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.PositiveIntegerField(default=0)
    answers = models.ManyToManyField(OptionQuest)

    class Meta:
        verbose_name = 'Попытка квеста'
        verbose_name_plural = 'Попытки квестов'
