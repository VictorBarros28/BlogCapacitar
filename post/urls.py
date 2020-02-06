from django.urls import path
from post.views import PostListView
app_name = 'post'

urlpatterns = [
     path('postagens',PostListView.as_view(),name = 'listar_postagens'),
    
]
