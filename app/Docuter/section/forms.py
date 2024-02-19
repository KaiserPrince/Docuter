from django import forms
from .models import Question, Option


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["section", "text"]


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ["question", "text"]
