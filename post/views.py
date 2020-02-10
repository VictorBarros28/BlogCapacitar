from django.shortcuts import render
from post.models import Post
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.views import generic
from django.urls import reverse_lazy
from post.forms import CreatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='post/postagem.html'


class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    template_name = 'post/create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('post:listar_postagens')

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post/delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('post:listar_postagens')

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['titulo','autor','content', 'img']
    template_name = 'post/update.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('post:listar_postagens')