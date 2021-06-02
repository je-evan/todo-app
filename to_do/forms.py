from django.forms import widgets
from to_do.models import Todo
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("task", "category", "due_date")
        widgets = {
            'due_date': DateInput(),
            }
