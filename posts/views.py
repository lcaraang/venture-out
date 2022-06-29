from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from django.http import JsonResponse
from django.db.models import Count

def jsondata(request):
    data = list(Post.objects.all().values('location').annotate(count=Count('location')))
    return JsonResponse(data, safe=False, content_type="application/json")

def map(request):
    return render(request, 'posts/map.html')

def landing(request):
    return render(request, 'posts/landing.html')

class HomeView(LoginRequiredMixin, generic.ListView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/home.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all posts."""
        return Post.objects.all().order_by('-date')

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
    fields = ['image', 'caption', 'location']
    success_url = reverse_lazy('posts:my-posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/update.html'
    model = Post
    fields = ['image', 'caption', 'location']
    success_url = reverse_lazy('posts:my-posts')

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts:my-posts')

class HawaiiFilteredView(generic.ListView):
    template_name = 'posts/hawaii.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(location='Hawaii').order_by('-date')

class KauaiFilteredView(generic.ListView):
    template_name = 'posts/kauai.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(location='Kauai').order_by('-date')

class LanaiFilteredView(generic.ListView):
    template_name = 'posts/lanai.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(location='Lanai').order_by('-date')

class MauiFilteredView(generic.ListView):
    template_name = 'posts/maui.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(location='Maui').order_by('-date')

class MolokaiFilteredView(generic.ListView):
    template_name = 'posts/Molokai.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(location='Molokai').order_by('-date')

class OahuFilteredView(generic.ListView):
    template_name = 'posts/oahu.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(location='Oahu').order_by('-date')

