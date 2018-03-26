from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from bookstore_management.forms import BookForm, UserForm
from bookstore_management.models import Book, RequestLog


def registration(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create_user(**user_form.cleaned_data)

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            ))

            return redirect('/')

    return render(request, 'my_auth/registration.html', {
        'user_form': user_form
    })


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {
        'books': books
    })


@login_required(login_url='login')
def books_management(request):
    books = Book.objects.all()
    return render(request, 'bookstore_management/books.html', {
        'books': books
    })


@login_required(login_url='login')
def create_book(request):
    book_form = BookForm
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect(books_management)
    return render(request, 'bookstore_management/book_form.html', {
        'book_form': book_form
    })


@login_required(login_url='login')
def update_book(request, book_id):
    book_form = BookForm(instance=Book.objects.get(id=book_id))
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect(books_management)
    return render(request, 'bookstore_management/book_form.html', {
        'book_form': book_form,
        'book_id': book_id
    })


@login_required(login_url='login')
def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect(books_management)


@login_required(login_url='login')
def request_log(request):
    requests = RequestLog.objects.all().order_by("-timestamp")[:10]
    return render(request, 'bookstore_management/request_log.html', {
        'requests': requests
    })