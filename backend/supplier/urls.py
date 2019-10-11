from django.urls import path

from . import views

app_name = 'supplier'

urlpatterns = [
    path('list/', views.SupplierListView.as_view(), name='list'),
    path('add/', views.SupplierListView.as_view(), name='add'),
    path('detail/<int:pk>/', views.SupplierDetailView.as_view(), name='details'),
    path('detail/<int:pk>/', views.SupplierDetailView.as_view(), name='edit'),
    path('detail/<int:pk>/', views.SupplierDetailView.as_view(), name='delete'),
    # path('product_category/list/', views.ProductCategoryView.as_view(), name='product_category_list'),
]
