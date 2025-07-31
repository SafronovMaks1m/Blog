from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     path('search/', views.post_search, name='post_search'),
     path('', views.post_list, name='post_list'),
     path('<int:year>/<int:month>/<int:day>/<slug:post>/',
          views.post_detail,
          name='post_detail'),
     path('<int:post_id>/share/',
          views.post_share, name='post_share'),
     path('<int:post_id>/comment/',
          views.post_comment, name='post_comment'),
     path('tag/<slug:tag_slug>/',
          views.post_list, name='post_list_by_tag')
]
{
    "id": 6,
    "author": 1,
    "title": "Проверка добавления поста",
    "body": "text of message",
    "created": "2025-07-28T18:49:34.87139",
    "status": "PB",
    "slug": "test-post"
}