from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, BibliotecaForm
from .models import Author, Book, Biblioteca




# Create your views here.
def home(request):
    return render(request, "froms_app/home.html")

def author_created (request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autor')
    else:
        form = BibliotecaForm()
    return render(request, 'froms/author.html', {'form': form})