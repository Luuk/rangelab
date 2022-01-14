from django import forms
from .models import Product, Member, MemberPresence, OrderProduct, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"

class MemberPresence(forms.ModelForm):
    class Meta:
        model = MemberPresence
        fields = "__all__"