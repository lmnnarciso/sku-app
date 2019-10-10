from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('list/', views.ProductView.as_view(), name='product'),
    path('add/', views.ProductView.as_view(), name='product_add'),
    path('product_category/add', views.ProductCategoryListView.as_view(), name='product_category_add'),
    path('product_category/list/', views.ProductCategoryListView.as_view(), name='product_category_list'),
    path('product_category/detail/<int:pk>/', views.ProductCategoryDetailView.as_view(), name='product_category_details'),
    path('product_supplier/list/', views.ProductSupplierListView.as_view(), name='product_supplier_list'),
    path('product_supplier/add/', views.ProductSupplierListView.as_view(), name='product_supplier_add'),
    # path('product_category/list/', views.ProductCategoryView.as_view(), name='product_category_list'),
]
