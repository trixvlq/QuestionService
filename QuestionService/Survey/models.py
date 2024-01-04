from django.contrib.auth.models import User
from django.db import models
from Question.models import Quiz, Question, Option


class Survey(Quiz):
    pass

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class QuestionSurvey(Question):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')

    class Meta:
        verbose_name = 'Вопрос опроса'
        verbose_name_plural = 'Вопросы опросов'


class OptionSurvey(Option):
    survey = models.ForeignKey(QuestionSurvey, on_delete=models.CASCADE, verbose_name='Опрос')

    class Meta:
        verbose_name = 'Ответ на опрос'
        verbose_name_plural = 'Ответы на опросы'


class SurveyAttempt(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    contender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Проходящий')
    chosen_options = models.ManyToManyField('OptionSurvey', verbose_name='Ответы')

    class Meta:
        verbose_name = 'Попытка прохождения опроса'
        verbose_name_plural = 'Попытки прохождений опросов'