from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('add/', views.add_entry, name='add'),
    path('history/', views.history, name='history'),
    path('stats/', views.stats, name='stats'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]