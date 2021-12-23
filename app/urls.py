from django.urls import path

from . import views

urlpatterns = [
    path('overview', views.overview, name='overview'),
    path('products', views.list_product, name='list_product'),
    path('products/create', views.create_product, name='create_product'),
    path('products/<int:id>', views.detail_product, name='detail_product'),
    path('products/<int:id>/update', views.update_product, name='update_product'),
    path('products/<int:id>/delete', views.delete_product, name='delete_product'),
    path('members', views.members, name='members'),
]
