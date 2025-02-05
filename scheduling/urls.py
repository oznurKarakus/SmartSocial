from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('templates/', views.manage_templates, name='manage_templates'),
    path('templates/create/', views.create_template, name='create_template'),
]
