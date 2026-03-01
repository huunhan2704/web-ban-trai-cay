from django.db import models

# 1. Bảng Danh mục - Phân loại trái cây (Nội địa, Nhập khẩu...) [cite: 6, 30, 31]
class Category(models.Model):
    name = models.CharField(max_length=100) # [cite: 33]
    slug = models.SlugField(unique=True) # [cite: 34]
    description = models.TextField(blank=True) # [cite: 35]

# 2. Bảng Sản phẩm - Lưu chi tiết từng loại trái cây [cite: 7, 36, 37]
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # [cite: 39]
    name = models.CharField(max_length=200) # [cite: 40]
    price = models.DecimalField(max_digits=10, decimal_places=0) # [cite: 41]
    unit = models.CharField(max_length=50) # kg, thùng, khay [cite: 42]
    stock_quantity = models.IntegerField(default=0) # [cite: 43]
    image = models.ImageField(upload_to='products/') # [cite: 44]
    description = models.TextField() # [cite: 45]
    is_featured = models.BooleanField(default=False) # Hiện ở mục bán chạy [cite: 46]

# 3. Bảng Đơn hàng - Lưu thông tin khách đặt mua [cite: 9, 56, 57]
class Order(models.Model):
    customer_name = models.CharField(max_length=200) # [cite: 59]
    customer_phone = models.CharField(max_length=15) # [cite: 60]
    customer_address = models.TextField() # [cite: 61]
    total_amount = models.DecimalField(max_digits=10, decimal_places=0) # [cite: 62]
    status = models.CharField(max_length=50, default='Chờ xác nhận') # [cite: 63]
    created_at = models.DateTimeField(auto_now_add=True) # [cite: 64]