from django.urls import path

from . import views

app_name = 'supplier'

urlpatterns = [
    path('list/', views.SupplierListView.as_view(), name='list'),
    path('add/', views.SupplierListView.as_view(), name='add'),
    # path('product_supplier/list/', views.ProductSupplierListView.as_view(), name='product_supplier_list'),
    # path('product_supplier/add/', views.ProductSupplierListView.as_view(), name='product_supplier_add'),
    # path('product_category/list/', views.ProductCategoryView.as_view(), name='product_category_list'),
]
