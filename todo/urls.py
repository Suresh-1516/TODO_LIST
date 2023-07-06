
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<num>',views.delete,name='delete'),
    path('edit/<num>',views.edit,name='edit'),
    path('add/',views.add,name='add'),
]
