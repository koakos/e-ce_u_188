from django.urls import path
from . import views

app_name = 'logger'

urlpatterns = [
    path('',views.index, name='index'),
    path('add_new_item/',views.ProductCreate.as_view(),name='add-new-item'),
    path('add_new_customer/',views.CustomerCreate.as_view(),name='add-new-customer'),
    path('Customers/',views.CustomerListView.as_view(),name='customer-list'),
    path('Sales/',views.SaleListView.as_view(),name='sales-list'),
    path('add_new_sale/',views.SaleCreate.as_view(),name='add-new-sale'),
    path('<slug:type>/',views.ProductListView.as_view(), name='product-list'),
    path('<slug:type>/backup/',views.backup_product_csv, name='backup_product_csv'),
    path('<slug:type>/<int:pk>/',views.ProductDetailView.as_view(), name='product-detail'),
    path('<slug:type>/<int:pk>/edit',views.ProductEditView.as_view(), name='product-update'),
    path('<slug:type>/<int:pk>/update/<slug:field>/',views.update_product_field, name='update-product-field'),
]
