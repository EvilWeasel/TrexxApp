import email
from django import forms
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=200)
    loghash = models.CharField(max_length=200, default='none')


class Lernobjekt(models.Model):
    name = models.CharField(max_length=200)
    beschreibung = models.CharField(max_length=200)
    kategorie = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(null=True)
