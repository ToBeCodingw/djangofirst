from django.urls import path
from .views import hello
from .views import booksAPI
urlpatterns = [
    path("hello/", hello),
    path("books/", booksAPI),
]