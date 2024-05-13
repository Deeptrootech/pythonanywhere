from django.shortcuts import render
from django.views.generic import ListView, CreateView

from app_bookstall.models import Book


# Create your views here.
class BookView(ListView):
    context_object_name = "book"
    model = Book
    template_name = "book_list.html"


class BookCreate(CreateView):
    model = Book
    fields = ["title", "authors", "publisher"]
    template_name = "add_book.html"
    success_url = "/books"

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
