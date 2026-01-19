from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('list/', views.basket_list, name='basket_list'),
    path('delete/<int:id>/', views.delete_from_basket, name='delete_from_basket'),
    path('edit/<int:id>/', views.edit_order, name='edit_order'),
]