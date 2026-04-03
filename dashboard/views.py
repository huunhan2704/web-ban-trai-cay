from django.shortcuts import render, redirect
from fruit_store.models import Product
from .forms import ProductForm

# 1. Trang danh sách sản phẩm
def product_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product_list.html', {'products': products})

# 2. Trang thêm sản phẩm mới
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'dashboard/product_form.html', {'form': form})