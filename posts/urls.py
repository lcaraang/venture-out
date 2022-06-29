from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home', views.HomeView.as_view(), name='home'),
    path('map', views.map, name='map'),
    path('hawaii', views.HawaiiFilteredView.as_view(), name='hawaii'),
    path('kauai', views.KauaiFilteredView.as_view(), name='kauai'),
    path('lanai', views.LanaiFilteredView.as_view(), name='lanai'),
    path('maui', views.MauiFilteredView.as_view(), name='maui'),
    path('molokai', views.MolokaiFilteredView.as_view(), name='molokai'),
    path('oahu', views.OahuFilteredView.as_view(), name='oahu'),
    path('my-posts', views.MyPostsView.as_view(), name='my-posts'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path("api/jsondata", views.jsondata, name="jsondata"),
]
