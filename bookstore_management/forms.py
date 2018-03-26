from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from django.contrib.auth.models import User
from bookstore_management.models import Book


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class BookForm(forms.ModelForm):
    publish_date = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Book
        fields = ['book_title', 'authors_info', 'ISBN', 'price', 'image', 'publish_date']





