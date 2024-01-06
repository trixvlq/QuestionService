# Generated by Django 5.0 on 2024-01-04 20:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionQuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('power', models.IntegerField(default=0, verbose_name='Значение опции')),
            ],
            options={
                'verbose_name': 'Вариант ответа квеста',
                'verbose_name_plural': 'Варианты ответов квестов',
            },
        ),
        migrations.CreateModel(
            name='QuestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_score', models.IntegerField(verbose_name='Минимальный порог')),
                ('max_score', models.IntegerField(verbose_name='Максимальный порог')),
                ('text', models.TextField(verbose_name='Текст с концовкой')),
                ('img', models.ImageField(blank=True, upload_to='static/images/%Y/%m/%d/', verbose_name='Картинка в конце')),
            ],
            options={
                'verbose_name': 'Конецовка теста',
                'verbose_name_plural': 'Концовки тестов',
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название вопроса')),
                ('q_amount', models.PositiveIntegerField(default=1, verbose_name='Количество вопросов')),
                ('description', models.TextField(verbose_name='Описание опроса')),
                ('pic', models.ImageField(blank=True, upload_to='static/images/%Y/%m/%d/', verbose_name='Картинка теста')),
                ('question_amount', models.IntegerField(default=0, verbose_name='Количество вопросов')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Квест',
                'verbose_name_plural': 'Квесты',
            },
        ),
        migrations.CreateModel(
            name='QuestAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveIntegerField(default=0)),
                ('answers', models.ManyToManyField(to='Quest.optionquest')),
                ('contender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quest.quest')),
            ],
            options={
                'verbose_name': 'Попытка квеста',
                'verbose_name_plural': 'Попытки квестов',
            },
        ),
        migrations.CreateModel(
            name='QuestionQuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quest.quest', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос квеста',
                'verbose_name_plural': 'Вопросы квеста',
            },
        ),
        migrations.AddField(
            model_name='optionquest',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quest.questionquest', verbose_name='Опрос'),
        ),
    ]
