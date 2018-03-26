from django.contrib import admin

# Register your models here.
from bookstore_management.models import Book, RequestLog

admin.site.register(Book)
admin.site.register(RequestLog)
