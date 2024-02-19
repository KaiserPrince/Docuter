from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Question(models.Model):
    # section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text = models.TextField()


class Option(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
