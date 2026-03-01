from django.db import models

# 1. Bảng Danh mục (Categories) [cite: 30]
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Mô tả")

    def __str__(self):
        return self.name

# 2. Bảng Sản phẩm (Products) [cite: 36]
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Danh mục")
    name = models.CharField(max_length=200, verbose_name="Tên trái cây")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá bán")
    unit = models.CharField(max_length=50, verbose_name="Đơn vị tính") # ví dụ: kg, thùng [cite: 42]
    stock_quantity = models.IntegerField(default=0, verbose_name="Số lượng tồn kho")
    image = models.ImageField(upload_to='products/', verbose_name="Ảnh sản phẩm")
    description = models.TextField(verbose_name="Mô tả chi tiết")
    is_featured = models.BooleanField(default=False, verbose_name="Sản phẩm nổi bật")

# 4. Bảng Đơn hàng (Orders) [cite: 56]
class Order(models.Model):
    customer_name = models.CharField(max_length=200, verbose_name="Tên người mua")
    customer_phone = models.CharField(max_length=15, verbose_name="Số điện thoại")
    customer_address = models.TextField(verbose_name="Địa chỉ giao hàng")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tổng tiền")
    status = models.CharField(max_length=50, default='Chờ xác nhận', verbose_name="Trạng thái")
    created_at = models.DateTimeField(auto_now_add=True)