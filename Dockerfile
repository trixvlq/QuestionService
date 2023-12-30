FROM python:3.10-alpine

COPY requirements.txt /temp/requirements.txt
COPY QuestionService /QuestionService

WORKDIR QuestionService

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password quiestion_user

USER question_user