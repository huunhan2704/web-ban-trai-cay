from django.shortcuts import get_object_or_404, render, redirect
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
# Hàm Sửa bài viết/sản phẩm
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/product_form.html', {'form': form, 'edit_mode': True})

# Hàm Xóa bài viết/sản phẩm
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'dashboard/product_confirm_delete.html', {'product': product})

from fruit_store.models import Product, News # Nhớ tạo model News như mình gửi ở trên

def news_list(request):
    all_news = News.objects.all().order_by('-created_at')
    return render(request, 'dashboard/news_list.html', {'news': all_news})

def news_add(request):
    # Logic tương tự như product_add nhưng dùng NewsForm
    pass

from fruit_store.models import Category # Nhớ import model Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category_list.html', {'categories': categories})

# Bạn có thể viết thêm hàm category_add tương tự như product_add

from fruit_store.models import Category
from .forms import CategoryForm

# 1. Trang danh sách danh mục
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category_list.html', {'categories': categories})

# 2. Trang thêm danh mục mới
def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/category_form.html', {'form': form})