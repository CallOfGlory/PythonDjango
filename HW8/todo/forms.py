from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time', 'category', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть назву завдання'}),
            'time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
