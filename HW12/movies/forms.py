from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_date', 'description', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'director': forms.TextInput(attrs={'class': 'form-input'}),
            'release_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}, format='%Y-%m-%d'),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'rating': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['release_date'].input_formats = ['%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y']