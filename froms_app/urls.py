from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='froms_app/home.html'),
    path('authors/', views.author_list, name='author'),
    path('authors/new/', views.author_create, name='author_create'),

    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_create, name='book_create'),


    path('biblioteca/new/', views.biblioteca_create, name='biblioteca_create'), 
]