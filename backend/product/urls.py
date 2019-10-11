from django.urls import path

from . import views

app_name = 'product'
# ProductSupplierDetailView
urlpatterns = [
    path('list/', views.ProductView.as_view(), name='product'),
    path('add/', views.ProductView.as_view(), name='product_add'),
    path('detail/<uuid:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('detail/<uuid:pk>/', views.ProductDetailView.as_view(), name='product_edit'),
    path('detail/<uuid:pk>/', views.ProductDetailView.as_view(), name='product_delete'),
    path('product_category/add', views.ProductCategoryListView.as_view(), name='product_category_add'),
    path('product_category/list/', views.ProductCategoryListView.as_view(), name='product_category_list'),
    path('product_category/detail/<int:pk>/', views.ProductCategoryDetailView.as_view(), name='product_category_details'),
    path('product_category/detail/<int:pk>/', views.ProductCategoryDetailView.as_view(), name='product_category_edit'),
    path('product_category/detail/<int:pk>/', views.ProductCategoryDetailView.as_view(), name='product_category_delete'),
    path('product_supplier/list/', views.ProductSupplierListView.as_view(), name='product_supplier_list'),
    path('product_supplier/add/', views.ProductSupplierListView.as_view(), name='product_supplier_add'),
    path('product_supplier/detail/<int:pk>/', views.ProductSupplierDetailView.as_view(), name='product_supplier_details'),
    path('product_supplier/detail/<int:pk>/', views.ProductSupplierDetailView.as_view(), name='product_supplier_edit'),
    path('product_supplier/detail/<int:pk>/', views.ProductSupplierDetailView.as_view(), name='product_supplier_delete'),
    path('product_stock/list/', views.ProductStockLevelView.as_view(), name='product_stock_list'),
    path('product_stock/add/', views.ProductStockLevelView.as_view(), name='product_stock_add'),
    path('product_stock/detail/<int:pk>/', views.ProductStockLevelDetailView.as_view(), name='product_stock_details'),
    path('product_stock/detail/<int:pk>/', views.ProductStockLevelDetailView.as_view(), name='product_stock_edit'),
    path('product_stock/detail/<int:pk>/', views.ProductStockLevelDetailView.as_view(), name='product_stock_delete'),
    # path('product_category/list/', views.ProductCategoryView.as_view(), name='product_category_list'),
]
