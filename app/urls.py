from django.urls import path

from . import views

urlpatterns = [
    path('overview', views.overview, name='overview'),
    path('products', views.products, name='products'),
    path('members', views.members, name='members'),
]