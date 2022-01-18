from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Product, Category
from .forms import ProductForm, CategoryForm

import csv
# Create your views here.

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'category_list'   # name for the list as a template variable
    queryset = Category.objects.all()
    template_name = 'inventory/view_categories.html'
    paginate_by = 10

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'   # name for the list as a template variable
    queryset = Product.objects.all()
    template_name = 'inventory/view_products.html'
    paginate_by = 10

def index(request):
    """View function for home page of site."""
    num_products = Product.objects.all().count()
    
    # Available products
    num_available_products = Product.objects.filter(total_quantity__gt = 0).count()

    context = {
        'num_products' : num_products,
        'num_avail_products' : num_available_products
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'inventory/index.html', context=context)

def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')
    
    context = { 'form' : form }
    return render(request, 'inventory/create_category.html', context)

def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    
    context = { 'form' : form }
    return render(request, 'inventory/create_product.html', context)

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance = product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('products')
    
    context = { 'form' : form }
    return render(request, 'inventory/edit_product.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {
        'product': product,
    }
    return render(request, 'inventory/delete_product.html', context)

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'inventory/detail_product.html', context={'product': product})

def export_data(request):
    response = HttpResponse(
        content_type='text/csv',
    )
    response['Content-Disposition'] = 'attachment; filename="table.csv"'
    fields = [f.name for f in Product._meta.fields]
    writer = csv.writer(response)
    # Write headers to CSV file    
    writer.writerow(fields)

    for row in Product.objects.values(*fields):
        writer.writerow([row[field] for field in fields])

    return response

def warehouse_detail(request, warehouse_id):
    return HttpResponse()

def customer_detail(request, customer_id):
    return HttpResponse()

def supplier_detail(request, supplier_id):
    return HttpResponse()

def shipment_detail(request, shipment_id):
    return HttpResponse()



