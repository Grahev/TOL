from django.contrib import admin
from django.urls import path, include
from authentication import views

app_name = 'authenticator'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
