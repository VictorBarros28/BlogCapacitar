from django.urls import path
from user.views import UserListView,UserCreateView,UserDeleteView,UserUpdateView
app_name = 'user'

urlpatterns = [
     path('usuarios',UserListView.as_view(),name = 'listar_usuarios'),
     path('criarusuario',UserCreateView.as_view(),name = 'criar_usuario'),
     path('usuarios/<int:pk>/apagar',UserDeleteView.as_view(),name = 'deletar_usuario'),
     path('usuarios/<int:pk>/editar',UserUpdateView.as_view(),name = 'editar_usuario'),
]

