from django.contrib import admin
from store.models import *
# Register your models here.

#admin.site.register(Book)
#admin.site.register(BookCopy)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookCopy) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'borrow_date')
    list_display = ('book','status', 'borrow_date')

admin.site.register(BookRating)
