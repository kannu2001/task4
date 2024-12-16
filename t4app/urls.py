from t4app import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('product',views.product),
    path('product_details/<pid>',views.product_details),
    path('search',views.search),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
