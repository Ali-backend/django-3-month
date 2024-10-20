from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('http_response/', views.http_response),
    path('http_response/', views.http_response),
    path('posts/', views.post_list_view),
    path('posts/<int:id>/', views.post_detail_view),
]