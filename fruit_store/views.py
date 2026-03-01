from django.shortcuts import render
from .models import Product

def home(request):
    # Lấy các sản phẩm nổi bật để hiện lên trang chủ [cite: 46]
    products = Product.objects.filter(is_featured=True)
    return render(request, 'fruit_store/home.html', {'products': products})