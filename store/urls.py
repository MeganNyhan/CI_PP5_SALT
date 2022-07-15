from django.urls import path
from . import views

urlpatterns = [
  path('checkout/', CheckOutView.as_view(), name='checkout'),
  path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
  path('product/<slug>/', ItemDetailView.as_view(), name='product'),
  path('add-to-cart/<slug>', get_add_to_cart, name='add-to-cart'),
  path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
  path('remove-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-item-from-cart'),
  path('payment/<payment_option>', PaymentView.as_view(), name='payment'),
]
