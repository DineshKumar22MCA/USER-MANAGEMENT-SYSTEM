from django.urls import path

from .views import insert, display, delete,edit

urlpatterns = [
    path('', display, name='display'),
    path('insert/', insert, name='insert'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]
