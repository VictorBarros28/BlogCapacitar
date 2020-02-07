from django.urls import path
from user.views import UserListView,UserCreateView
app_name = 'user'

urlpatterns = [
     path('usuarios',UserListView.as_view(),name = 'listar_usuarios'),
     path('criarusuario',UserCreateView.as_view(),name = 'criar_usuario'),
]

