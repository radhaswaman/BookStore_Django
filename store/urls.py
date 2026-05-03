from django.urls import path

from .views import UserLoginView, UserLogoutView, book_detail, catalogue, home, register

urlpatterns = [
    path("", home, name="home"),
    path("catalogue/", catalogue, name="catalogue"),
    path("books/<int:book_id>/", book_detail, name="book_detail"),
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
