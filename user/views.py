from django.shortcuts import render
from user.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from user.forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name='user/usuario.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'user/create.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('user:listar_usuarios')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/delete.html'
    context_object_name = 'users'
    success_url = reverse_lazy('user:listar_usuarios')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username','email','password']
    template_name = 'user/update.html'
    context_object_name = 'users'
    success_url = reverse_lazy('user:listar_usuarios')

class UserDetailView(DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'User'

class UserLoginView(LoginView):
    template_name = 'user/login.html'

class UserLogoutView(LoginRequiredMixin,LogoutView):
    pass

    

