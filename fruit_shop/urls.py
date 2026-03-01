from django.contrib import admin
from django.urls import path
from django.conf import settings # Thêm dòng này
from django.conf.urls.static import static # Thêm dòng này
from fruit_store.views import home # Đảm bảo đã import view trang chủ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
] 

# Đoạn này giúp hiển thị ảnh sản phẩm và banner từ thư mục media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)