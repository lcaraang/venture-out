from django.views import generic
from django.urls import reverse_lazy
from .models import Post

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all posts."""
        return Post.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'posts/create.html'
    model = Post
    fields = ['user', 'image', 'caption']
    success_url = reverse_lazy('posts:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['user', 'image', 'caption']
    success_url = reverse_lazy('posts:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts:index')
