from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('list/', views.ProductView.as_view(), name='product'),
]
