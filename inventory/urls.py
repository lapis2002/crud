from django.urls import path

from . import views

urlpatterns = [
    # /inventory/
    path('', views.index, name='index'),  
    #/inventory/categories/                                         
    path('categories/', views.CategoryListView.as_view(), name='categories'),  
    # /inventory/products/
    path('products/', views.ProductListView.as_view(), name='products'),                                    
    # /inventory/export
    path('export', views.export_data, name='export_csv'),
    # /inventory/categories/create
    path('categories/create/', views.create_category, name='create_category'),
    # /inventory/products/create
    path('products/create/', views.create_product, name='create_product'),
    #/inventory/product/1/update                                         
    path('product/<uuid:product_id>/update/', views.update_product, name='update_product'),
    #/inventory/product/1                                         
    path('product/<uuid:product_id>/delete/', views.delete_product, name='delete_product'),
    #/inventory/product/1                                         
    path('product/<uuid:product_id>/', views.product_detail_view, name='product_detail'),
    # #/inventory/warehouses/                                         
    # path('warehouses/', views.WarehouseListView.as_view(), name='warehouses'),
    # #/inventory/customers/                                      
    # path('customers/', views.CustomerListView.as_view(), name='customers'),
    # #/inventory/suppliers/                                         
    # path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    # #/inventory/receipts/                                         
    # path('receipts/', views.ReceiptListView.as_view(), name='receipts'),
    # #/inventory/deliveries/                                         
    # path('deliveries/', views.DeliveryListView.as_view(), name='deliveries'),
    # #/inventory/warehouse/1                                         
    # path('warehouse/<uuid:warehouse_id>/', views.WarehouseListView.as_view(), name='warehouses'),
    # #/inventory/customer/1                                         
    # path('customer/<uuid:customer_id>/', views.CustomerListView.as_view(), name='customers'),
    # #/inventory/supplier/1                                         
    # path('supplier/<uuid:supplier_id>/', views.SupplierDListView.as_view(), name='suppliers'),
    # #/inventory/shipment/1                                         
    # path('shipment/<uuid:shipment_id>/', views.ShipmentListView.as_view(), name='shipments')      
]