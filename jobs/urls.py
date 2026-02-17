from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='jobs.index'),
    path('apply/<int:id>', views.apply, name='jobs.apply'),
    path('create/', views.create_or_edit, name='jobs.create'),
    path('edit/<int:id>', views.create_or_edit, name='jobs.edit'),
]