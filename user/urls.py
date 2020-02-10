from django.urls import path
from user.views import UserListView,UserCreateView,UserDeleteView,UserUpdateView,UserDetailView,UserLoginView,UserLogoutView
app_name = 'user'

urlpatterns = [
     path('usuarios',UserListView.as_view(),name = 'listar_usuarios'),
     path('criarusuario',UserCreateView.as_view(),name = 'criar_usuario'),
     path('usuarios/<int:pk>/apagar',UserDeleteView.as_view(),name = 'deletar_usuario'),
     path('usuarios/<int:pk>/editar',UserUpdateView.as_view(),name = 'editar_usuario'),
     path('usuarios/<int:pk>/detalhar',UserDetailView.as_view(),name = 'detalhar_usuario'),
     path('usuarios/login',UserLoginView.as_view(),name='logar_usuario'),
     path('usuarios/logout',UserLogoutView.as_view(),name = 'deslogar_usuario'),
]

