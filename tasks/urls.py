from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('update/<int:id>/', views.update_status, name='update_status'),
    path('list/', views.list_users, name='list_users'),
    path('sort/',views.sort_users,name='sort_users'),
    
]