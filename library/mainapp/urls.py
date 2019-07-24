from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home),
    path('accounts/addbook/',views.add_book, name="addbook"),
    path('booklist/',views.booklist),
    path('accounts/login/',LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/logout/',LogoutView.as_view(), name="logout"),
    path('accounts/profile/',TemplateView.as_view(template_name="admin.html"),name='profile'),
    path('accounts/reviewuser/',views.reviewuser,name="reviewuser"),
    path('accounts/bookdue/',views.bookdue,name="bookdue"),
    path('accounts/searchbook/',views.searchbook,name="searchbook"),
    path('accounts/renewbook/<pk>/',views.renewbook,name="renewbook"),
    path('accounts/allotbook/<pk>/',views.allotbook,name="allotbook"),
    path('accounts/makeavailable/<pk>/',views.makeavailable,name="makeavailable"),
    path('accounts/aproveuser/<pk>/',views.aproveuser,name="aproveuser"),
    path('accounts/deleteuser/<pk>/',views.deleteuser,name="deleteuser"),
    path('accounts/searchuser/',views.searchuser,name="searchuser"),
    

]
