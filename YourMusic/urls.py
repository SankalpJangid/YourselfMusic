from django.contrib import admin
from django.urls import path,include
from YourMusic import views

urlpatterns = [
    path('',views.home, name="home"),
    path('search', views.search, name="search"),
    path('second', views.whole, name="second"),
    path('next/<int:id>', views.next, name="next"),
]