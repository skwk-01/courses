from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('edit_memo/', views.edit_memo, name='edit_memo'),
    path('add/', views.add_times, name='add_times'), 
    path('decrease/', views.decrease_times, name='decrease_times'),
    path('setting/', views.setting, name='setting'),
    path('new/', views.add_courses, name='add_courses'),
    path('delete/<int:pk>/', views.delete_courses, name='delete_courses'),
    path('add/<int:pk>/', views.add_times, name='add_times'),  
    path('decreace/<int:pk>/', views.decrease_times, name='decrease_times'), 
]
