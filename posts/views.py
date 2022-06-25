from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Post

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all posts."""
        return Post.objects.all()

class HomeView(LoginRequiredMixin, generic.ListView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/home.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all posts."""
        return Post.objects.all().order_by('-date')

def map(request):
    return render(request, 'posts/map.html')

class MyPostsView(LoginRequiredMixin, generic.ListView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/my-posts.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all posts from user."""
        return Post.objects.filter(user=self.request.user).order_by('-date')

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/create.html'
    model = Post
    fields = ['image', 'caption']
    success_url = reverse_lazy('posts:my-posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/update.html'
    model = Post
    fields = ['image', 'caption']
    success_url = reverse_lazy('posts:my-posts')

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts:my-posts')
