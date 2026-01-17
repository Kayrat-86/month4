from django.urls import path
from . import views

urlpatterns = [
    path('products_one/', views.first_products),
    path('products_two/', views.second_products),
    path('products_three/', views.third_products),

    path('products_list/', views.products),
    path('products_list/<int:id>/', views.products_detail),
]
