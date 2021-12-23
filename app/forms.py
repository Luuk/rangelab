from django import forms
from .models import Product, Member


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"