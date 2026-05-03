from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "price", "stock")
    list_filter = ("genre",)
    search_fields = ("title", "author")
