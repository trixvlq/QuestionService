from django.contrib.auth.models import User
from django.db import models
from Question.models import Quiz, Question, Option


class Test(Quiz):
    question_amount = models.IntegerField(default=0, verbose_name='Количество вопросов')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class QuestionTest(Question):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Опрос')
    multiple_correct = models.BooleanField(default=False, verbose_name='Несколько правильных ответов')
    multiple_answers = models.BooleanField(default=False, verbose_name='Несколько ответов для засчёта')

    class Meta:
        verbose_name = 'Вопрос теста'
        verbose_name_plural = 'Вопросы тестов'


class OptionTest(Option):
    test = models.ForeignKey(QuestionTest, on_delete=models.CASCADE, verbose_name='Опрос')
    correct = models.BooleanField(default=False, verbose_name='Правильность опции')

    class Meta:
        verbose_name = 'Вариант ответа теста'
        verbose_name_plural = 'Варианты ответов тестов'


class TestAttempt(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Опрос')
    contender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Проходящий')
    result = models.PositiveIntegerField(default=0, verbose_name='Результат')
    chosen_options = models.ManyToManyField(OptionTest, verbose_name='Выбранные ответы')

    class Meta:
        verbose_name = 'Попытка теста'
        verbose_name_plural = 'Попытки тестов'
