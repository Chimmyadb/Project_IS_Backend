
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import manage_customer, manage_product, manage_order, manage_order_item, manage_supplier

urlpatterns = [
    path('customers/', manage_customer, name='get_customers'),
    path('customer/<int:id>/', manage_customer, name='get_customer'),

    path('products/', manage_product, name='get_products'),
    path('product/<int:id>/', manage_product, name='get_product'),

    path('orders/', manage_order, name='get_orders'),
    path('order/<int:id>/', manage_order, name='get_order'),

    path('order-items/', manage_order_item, name='get_order_items'),
    path('order-item/<int:id>/', manage_order_item, name='get_order_item'),

    path('suppliers/', manage_supplier, name='get_suppliers'),
    path('supplier/<int:id>/', manage_supplier, name='get_supplier'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

