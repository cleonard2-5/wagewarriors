from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='account.index'),
    path('signup/seeker', views.seeker_signup, name='account.seeker_signup'),
    path('signup/recruiter', views.recruiter_signup, name='account.recruiter_signup'),
    path('profile/<str:username>/', views.profile, name='account.profile'),
    path('profile/<str:username>/edit', views.edit_profile, name='account.edit_profile'),
    path('applications/<str:username>/', views.applications, name='account.applications'),
    path('login/', views.login_view, name='account.login'),
    path('logout/', views.logout_view, name='account.logout'),
]