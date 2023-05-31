from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home" ),
    path('articles/', views.articles, name="articles"),
    path('about/', views.about_us, name="about_us"),
    path('details/<int:pk>/', views.articles_details, name="details"),
    
    path('create/', views.articles_create, name="create"),
    path('update/<int:pk>/', views.article_update, name="update"),
    path('delete/<int:pk>/', views.article_delete, name="delete"),
    
]


