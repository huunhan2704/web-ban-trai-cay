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
def san_pham(request):
    # Lấy toàn bộ sản phẩm từ Database
    all_products = Product.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'fruit_store/san_pham.html', {
        'products': all_products,
        'categories': categories
    })
def tin_tuc(request):
    # Giả sử bạn đã có model News, nếu chưa có thể dùng Product tạm thời để test layout
    # news_list = News.objects.all().order_by('-created_at')
    return render(request, 'fruit_store/tin_tuc.html')
def gio_hang(request):
    # Logic lấy sản phẩm từ session (giỏ hàng tạm thời) sẽ viết ở đây
    return render(request, 'fruit_store/gio_hang.html')

def gioi_thieu(request):
    return render(request, 'fruit_store/gioi_thieu.html')