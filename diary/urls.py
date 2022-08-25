from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
    blog_post_create_view
)

urlpatterns = [
    path('', blog_post_list_view, name='diary'),
    path('create/', blog_post_create_view, name='create'),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
]
