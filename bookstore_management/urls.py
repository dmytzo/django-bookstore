from django.urls import path

from bookstore_management import views

urlpatterns = [
    path('books', views.books_management, name='books-management'),
    path('books/add', views.create_book, name='create-book'),
    path('books/<int:book_id>/update', views.update_book, name='update-book'),
    path('books/<int:book_id>/delete', views.delete_book, name='delete-book'),
    path('request-log', views.request_log, name='request-log'),
]