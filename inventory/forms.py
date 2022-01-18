# import form class from django
from django import forms
from django.forms import ModelForm
from .models import Category, Product
  
# create a ModelForm
class CategoryForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Category
        fields = "__all__"

class ProductForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            # 'unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            # 'total_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
            # 'sold': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'category_id': forms.CheckboxSelectMultiple(),
        }