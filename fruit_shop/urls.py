from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from fruit_store import views # Import tất cả views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('san-pham/', views.san_pham, name='san_pham'),
    path('tin-tuc/', views.tin_tuc, name='tin_tuc'),   
    path('gio-hang/', views.gio_hang, name='gio_hang'),
] 

# Đoạn này CỰC KỲ QUAN TRỌNG để hiện ảnh từ thư mục media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)