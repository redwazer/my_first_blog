from django.urls import path
from . import views
urlpatterns = [
#path('',views.index, name='index')

# path('post',views.post_list, name='post'),
path('', views.News_page, name="main"),
path("News_page", views.News_page, name="News_page"),
path("sportspage", views.sportspage, name="sportspage")


]