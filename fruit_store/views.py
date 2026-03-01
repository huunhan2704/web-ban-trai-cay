from django.shortcuts import render
from .models import Product, Category

def home(request):
    # Lấy tất cả danh mục có chứa sản phẩm
    categories = Category.objects.all()
    # Lấy sản phẩm nổi bật
    products = Product.objects.filter(is_featured=True)
    
    return render(request, 'fruit_store/home.html', {
        'categories': categories,
        'products': products
    })