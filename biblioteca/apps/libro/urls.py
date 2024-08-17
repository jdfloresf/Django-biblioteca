from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.LibrosListView.as_view(), name='libros'),
    path('libros2/', views.Libros2ListView.as_view(), name='libros2'),
    path('libro-detalle/<pk>/', views.LibroDetailView.as_view(), name='libros_detalle')
]