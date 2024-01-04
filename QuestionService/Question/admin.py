from django.contrib import admin
from .models import *
from Quest.models import *
from Test.models import *
from Survey.models import *



admin.site.register(Test)
admin.site.register(Survey)
admin.site.register(Quest)
admin.site.register(QuestionTest)
admin.site.register(QuestionSurvey)
admin.site.register(QuestionQuest)
admin.site.register(OptionTest)
admin.site.register(OptionSurvey)
admin.site.register(OptionQuest)
admin.site.register(QuestAttempt)
admin.site.register(TestAttempt)
admin.site.register(SurveyAttempt)
