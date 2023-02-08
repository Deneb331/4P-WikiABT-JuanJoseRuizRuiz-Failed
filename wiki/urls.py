from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('', views.PostList.as_view(), name='post_list'),
    path('', views.PostView.as_view(), name='post_view'),
    path('about-us/', views.AboutUs.as_view(), name='about_us'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('<slug:slug>/', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.CategoryList.as_view(), name='category_list'),
]