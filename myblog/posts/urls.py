from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.posts_list, name='posts'),
    path('new-post/', views.post_new, name='new-post'),
    path('post/<slug:slug>/', views.post_page, name='page'),
    path('post/<slug:slug>/edit/', views.post_edit, name='edit'),
    path('<slug:slug>/delete/', views.post_delete, name='delete'),
]