from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayEvents, name='home'),
    path('create/', views.createEvent, name='create_event'),
    path('edit/<int:id>/', views.editEvent, name='edit_event'),
    path('delete/<int:id>/', views.deleteEvent, name='delete_event'),
    path('category/<str:category>/', views.filterEvent, name='filter_event'),
]