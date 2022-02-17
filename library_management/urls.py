from django.contrib import admin
from django.urls import path
from library_management import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("sinup/",views.signup, name="sinup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
    path("details/", views.details, name="details"),
    path('books/', views.books , name='books'),
    path("add_book", views.add_book, name="add_book"),
]