from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, RegisterForm
from .models import Book


def home(request):
    featured_books = Book.objects.all()[:3]
    return render(request, "store/home.html", {"featured_books": featured_books})


def catalogue(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    context = {
        "books": books,
        "query": query,
    }
    return render(request, "store/catalogue.html", context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "store/book_detail.html", {"book": book})


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome to BookHaven.")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "store/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "store/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = "home"
