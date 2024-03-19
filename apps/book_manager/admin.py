from django.contrib import admin
from apps.book_manager.models import Book
from apps.book_manager.backend.book_admin import BookAdmin

admin.site.register(Book, BookAdmin)
