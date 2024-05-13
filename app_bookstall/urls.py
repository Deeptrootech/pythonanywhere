from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from app_bookstall.views import BookView, BookCreate

urlpatterns = [
    path("", BookView.as_view(), name="book-list"),
    path("add_book/", BookCreate.as_view(), name="book-create"),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
