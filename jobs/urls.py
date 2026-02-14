from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='jobs.index'),
    path('apply/<int:id>', views.apply, name='jobs.apply'),
]