from django import forms
from .models import Author, Book, Biblioteca


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name',]
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors',] 
 
class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = '__all__'              