from django.urls import path
from post.views import PostListView,PostCreateView,PostDeleteView,PostUpdateView
app_name = 'post'

urlpatterns = [
     path('postagens',PostListView.as_view(),name = 'listar_postagens'),
     path('criarpostagem',PostCreateView.as_view(),name = 'criar_postagem'),
     path('postagens/<int:pk>/apagar',PostDeleteView.as_view(),name = 'deletar_postagem'),
     path('postagens/<int:pk>/editar',PostUpdateView.as_view(),name = 'editar_postagem'),
]
