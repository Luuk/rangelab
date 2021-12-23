from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Product, Member
from django.contrib import messages
from .forms import ProductForm
from django.shortcuts import get_object_or_404


# OVERVIEW
@login_required(login_url='login')
def overview(request):
    return render(request, 'app/overview.html')


# PRODUCTS
@login_required(login_url='login')
def list_product(request):
    products = Product.objects.all()
    return render(request, 'app/products/list.html', {'products': products})


@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Product toegevoegd!'))
            return redirect('/products')
        else:
            messages.success(request, form.errors)
            return render(request, 'app/products/create.html', {'product': product})
    else:
        return render(request, 'app/products/create.html')


@login_required(login_url='login')
def detail_product(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, 'app/products/detail.html', {'product': product})


@login_required(login_url='login')
def update_product(request, id):
    if request.method == 'POST':
        instance = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            product = Product.objects.filter(id=id).first()
            messages.success(request, ('Product gewijzigd!'))
            return render(request, 'app/products/update.html', {'product': product})
        else:
            product = Product.objects.filter(id=id).first()
            messages.success(request, form.errors)
            return render(request, 'app/products/update.html', {'product': product})
    else:
        product = Product.objects.filter(id=id).first()
        return render(request, 'app/products/update.html', {'product': product})


@login_required(login_url='login')
def delete_product(request, id):
    Product.objects.filter(id=id).delete()
    messages.success(request, ('Product verwijderd!'))
    return redirect('/products')


# MEMBERS
@login_required(login_url='login')
def members(request):
    members = Member.objects.all()
    return render(request, 'app/members.html', {'members': members})
