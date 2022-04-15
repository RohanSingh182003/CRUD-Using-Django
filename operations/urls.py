from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('delete/<int:del_id>',views.delete,name='delete'),
    path('update/<int:upd_id>',views.update,name='update'),
]