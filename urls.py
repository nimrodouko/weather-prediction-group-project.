from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homeview, name='predict'),
    path('result/', views.Ndaniyaform, name='result'),
]  