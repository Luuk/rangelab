from django.contrib import admin
from .models import Product, Member, MemberPresence, OrderProduct, Order

admin.site.register(Product)
admin.site.register(Member)
admin.site.register(MemberPresence)
admin.site.register(OrderProduct)
admin.site.register(Order)
