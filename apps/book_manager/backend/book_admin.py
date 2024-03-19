from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'price')

    change_list_template = 'admin/book_manager/book/change_list.html'
