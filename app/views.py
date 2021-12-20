from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def overview(request):
    return render(request, 'app/overview.html')

@login_required(login_url='login')
def products(request):
    return render(request, 'app/overview.html')

@login_required(login_url='login')
def members(request):
    return render(request, 'app/overview.html')