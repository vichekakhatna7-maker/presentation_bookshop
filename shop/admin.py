from django.contrib import admin
from .models import Author, Book, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "price", "stock")
    list_filter = ("category", "author")
    search_fields = ("title", "isbn", "author__name")

admin.site.register(Author)
admin.site.register(Category)

# Register your models here.
