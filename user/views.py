from django.shortcuts import render
from user.models import User
from django.views.generic import ListView,CreateView
from user.forms import CreateUserForm
from django.urls import reverse_lazy


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name='user/usuario.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'user/create.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('user:listar_usuarios')
    

