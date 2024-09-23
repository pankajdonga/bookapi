from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.getall),
    path('getid/<int:id>',views.getid),
    path('savedata/',views.savedata),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]