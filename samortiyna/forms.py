from django import forms
from models import Book


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", 'descriptions', 'author', 'published_date', 'isbn', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Ввкдіть заголовок'}),
            'created_at': forms.DateTimeField(attrs={'class': "form-control", 'placeholder': 'Створено о '}),
            'author': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Автор'}),
            'isbn': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'НОмер'}),
            'published_date': forms.DateField(attrs={'class': "form-control", 'placeholder': 'опубліковано о'}),
            'descriptions': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Опис'}),
        }
