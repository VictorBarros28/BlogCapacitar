from django.urls import path
from user.views import UserListView
app_name = 'user'

urlpatterns = [
     path('usuarios',UserListView.as_view(),name = 'listar_usuarios'),
    
]

