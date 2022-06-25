from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home', views.HomeView.as_view(), name='home'),
    path('my-posts', views.MyPostsView.as_view(), name='my-posts'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
]
