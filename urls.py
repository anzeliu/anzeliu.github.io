from django.urls import path
import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('projects', views.projects, name='projects')
]
