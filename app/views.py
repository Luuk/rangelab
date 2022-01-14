from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Product, Member, MemberPresence, OrderProduct, Order
from django.contrib import messages
from .forms import ProductForm, MemberForm
from django.shortcuts import get_object_or_404
import os
import datetime


def view_404(request, exception=None):
    return redirect('list_product')


# OVERVIEW
@login_required(login_url='login')
def overview(request):
    return render(request, 'app/management/overview.html')


# PRODUCTS
@login_required(login_url='login')
def list_product(request):
    products = Product.objects.filter(active=True)
    return render(request, 'app/management/products/list.html', {'products': products})


@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        form.active = False
        if form.is_valid():
            instance = form.save(commit=False)
            instance.active = True
            instance.save()
            messages.success(request, ('Product toegevoegd!'))
            return redirect('list_product')
        else:
            messages.success(request, form.errors)
            return render(request, 'app/management/products/create.html', {"form_data": request.POST})
    else:
        return render(request, 'app/management/products/create.html')


@login_required(login_url='login')
def detail_product(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, 'app/management/products/detail.html', {'product': product})


@login_required(login_url='login')
def update_product(request, id):
    if request.method == 'POST':
        product = Product.objects.filter(id=id).first()
        instance = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            if request.FILES:
                try:
                    os.remove(str(product.picture))
                except:
                    pass
            instance = form.save(commit=False)
            instance.active = True
            instance.save()
            product = Product.objects.filter(id=id).first()
            messages.success(request, ('Product gewijzigd!'))
            return render(request, 'app/management/products/update.html', {'product': product})
        else:
            product = Product.objects.filter(id=id).first()
            messages.success(request, form.errors)
            return render(request, 'app/management/products/update.html', {'product': product})
    else:
        product = Product.objects.filter(id=id).first()
        return render(request, 'app/management/products/update.html', {'product': product})


@login_required(login_url='login')
def delete_product(request, id):
    # try:
    #     os.remove(str(Product.objects.filter(id=id).first().picture))
    # except:
    #     pass
    Product.objects.filter(id=id).update(active=False)
    messages.success(request, ('Product verwijderd!'))
    return redirect('list_product')


# MEMBERS
@login_required(login_url='login')
def list_member(request):
    members = Member.objects.filter(active=True)
    return render(request, 'app/management/members/list.html', {'members': members})


@login_required(login_url='login')
def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.active = True
            instance.save()
            messages.success(request, ('Lid toegevoegd!'))
            return redirect('list_member')
        else:
            messages.success(request, form.errors)
            return render(request, 'app/management/members/create.html', {"form_data": request.POST})
    else:
        return render(request, 'app/management/members/create.html')


@login_required(login_url='login')
def detail_member(request, id):
    member = Member.objects.filter(id=id).first()
    return render(request, 'app/management/members/detail.html', {'member': member})


@login_required(login_url='login')
def update_member(request, id):
    if request.method == 'POST':
        member = Member.objects.filter(id=id).first()
        instance = get_object_or_404(Member, id=id)
        form = MemberForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            if request.FILES:
                try:
                    os.remove(str(member.picture))
                except:
                    pass
            instance = form.save(commit=False)
            instance.active = True
            instance.save()
            member = Member.objects.filter(id=id).first()
            messages.success(request, ('Lid gewijzigd!'))
            return render(request, 'app/management/members/update.html', {'member': member})
        else:
            member = Member.objects.filter(id=id).first()
            messages.success(request, form.errors)
            return render(request, 'app/management/members/update.html', {'member': member})
    else:
        member = Member.objects.filter(id=id).first()
        return render(request, 'app/management/members/update.html', {'member': member})


@login_required(login_url='login')
def delete_member(request, id):
    # try:
    #     os.remove(str(Member.objects.filter(id=id).first().picture))
    # except:
    #     pass
    Member.objects.filter(id=id).update(active=False)
    messages.success(request, ('Lid verwijderd!'))
    return redirect('list_member')


# PRESENCE
@login_required(login_url='login')
def list_presence(request):
    members = Member.objects.order_by("first_name").filter(active=True)
    present_member_ids = MemberPresence.objects.filter(is_present=True).values_list('member_id', flat=True)
    return render(request, 'app/cashier/presence/list.html',
                  {'members': members, 'present_member_ids': present_member_ids})


@login_required(login_url='login')
def update_presence(request, member_id):
    member_present = MemberPresence.objects.filter(member_id=member_id, is_present=True).first()

    if member_present:
        member_present.is_present = False
        member_present.save()
    else:
        member_presence = MemberPresence()
        member_presence.member_id = Member.objects.filter(id=member_id).first()
        member_presence.is_present = True
        member_presence.save()

    return redirect('list_presence')


# CASHIER
@login_required(login_url='login')
def list_present(request):
    present_member_ids = MemberPresence.objects.filter(is_present=True).values_list('member_id', flat=True)
    members = Member.objects.filter(pk__in=present_member_ids)
    return render(request, 'app/cashier/present/list.html', {'members': members})


@login_required(login_url='login')
def detail_present(request, member_id):
    order = Order.objects.filter(member_id=member_id, paid=False).first()
    total_price = 0

    if order:
        order_products = OrderProduct.objects.filter(order_id=order.id).all()
        for order_product in order_products:
            total_price = total_price + (order_product.product_price * order_product.quantity)
    else:
        order_products = []

    member = Member.objects.filter(id=member_id).first()
    products = Product.objects.order_by("name").filter(active=True)
    return render(request, 'app/cashier/present/detail.html',
                  {'member': member, 'products': products, 'order': order, 'order_products': order_products,
                   'total_price': total_price})


@login_required(login_url='login')
def create_order(request, member_id, product_id):
    order = Order.objects.filter(member_id=member_id, paid=False).first()
    product = Product.objects.filter(id=product_id).first()

    if not order:
        order = Order()
        order.member_id = Member.objects.filter(id=member_id).first()
        order.save()

    if order:
        order_products = OrderProduct.objects.filter(order_id=order.id, product_id=product_id).first()
        if order_products:
            order_products.quantity = order_products.quantity + 1
            order_products.save()
        else:
            order_product = OrderProduct()
            order_product.order_id = Order.objects.filter(id=order.id).first()
            order_product.product_id = product
            order_product.product_picture_url = product.picture
            order_product.product_name = product.name
            order_product.product_description = product.description
            order_product.product_code = product.code
            order_product.product_price = product.price
            order_product.quantity = 1
            order_product.save()
    return redirect('detail_present', member_id)


@login_required(login_url='login')
def increase_product_quantity(request, member_id, product_id):
    order = Order.objects.filter(member_id=member_id, paid=False).first()
    order_products = OrderProduct.objects.filter(order_id=order.id, product_id=product_id).first()
    order_products.quantity = order_products.quantity + 1
    order_products.save()
    return redirect('detail_present', member_id)


@login_required(login_url='login')
def decrease_product_quantity(request, member_id, product_id):
    order = Order.objects.filter(member_id=member_id, paid=False).first()
    order_products = OrderProduct.objects.filter(order_id=order.id, product_id=product_id).first()

    if order_products.quantity - 1 > 0:
        order_products.quantity = order_products.quantity - 1
        order_products.save()
    else:
        order_products.delete()
    return redirect('detail_present', member_id)
