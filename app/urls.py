from django.urls import path
from . import views

urlpatterns = [
    # OVERVIEW
    path('manage/overview', views.overview, name='overview'),

    # PRODUCTS
    path('manage/products', views.list_product, name='list_product'),
    path('manage/products/create', views.create_product, name='create_product'),
    path('manage/products/<int:id>', views.detail_product, name='detail_product'),
    path('manage/products/<int:id>/update', views.update_product, name='update_product'),
    path('manage/products/<int:id>/delete', views.delete_product, name='delete_product'),

    # MEMBERS
    path('manage/members', views.list_member, name='list_member'),
    path('manage/members/create', views.create_member, name='create_member'),
    path('manage/members/<int:id>', views.detail_member, name='detail_member'),
    path('manage/members/<int:id>/update', views.update_member, name='update_member'),
    path('manage/members/<int:id>/delete', views.delete_member, name='delete_member'),

    # PRESENCE
    path('cashier/presence', views.list_presence, name='list_presence'),
    path('cashier/presence/<int:member_id>/update', views.update_presence, name='update_presence'),

    # CASHIER
    path('cashier/present', views.list_present, name='list_present'),
    path('cashier/present/<int:member_id>', views.detail_present, name='detail_present'),
    path('cashier/present/<int:member_id>/order/<int:product_id>', views.create_order, name='create_order'),
    path('cashier/present/<int:member_id>/order/<int:product_id>/increase', views.increase_product_quantity, name='increase_product_quantity'),
    path('cashier/present/<int:member_id>/order/<int:product_id>/decrease', views.decrease_product_quantity, name='decrease_product_quantity'),
]
