"""
URL mappings for the User API.
"""
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'), # .as_view() is used bcz path is expecting a function instead of class , so as_view() will convert class based view into function.
    path('token/', views.CreateTokenView.as_view(), name='token'),
    ]