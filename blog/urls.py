from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('search/', views.search, name='search'),
    path('category/<slug:slug>/', views.category_posts, name='category'),
    path('tag/<slug:slug>/', views.tag_posts, name='tag'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
