from django.contrib import admin
from django.urls import path, include
from tracker import views

app_name = 'tracker'

urlpatterns = [
    path('api/all', views.project_list_api),
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('engineer/', views.project_by_engineer, name='project_list_by_engineer'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/note/create/', views.create_note, name='create_note'),
    path('note/delete/<int:pk>', views.delete_note, name='delete_note'),
    path('<int:pk>/update_status/<str:status>/', views.update_project_status, name='update_project_status'),
    path('<int:pk>/pe/', views.project_engineer_assign, name='project_engineer_assign')
]