from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'price')
