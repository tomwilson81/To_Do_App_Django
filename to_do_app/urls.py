from django.urls import path
from . import views

app_name = 'to_do_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('complete/<pk>/', views.complete, name='complete'),
    path('undo/<pk>/', views.undo, name='undo'),
    path('delete/<pk>/', views.delete, name='delete'),
]