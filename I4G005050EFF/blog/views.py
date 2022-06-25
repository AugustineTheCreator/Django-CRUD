# from django.shortcuts import render
from msilib.schema import ListView
from pyexpat import model
from django.views.generic.edit import CreateView
from .models import Post, blog
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')