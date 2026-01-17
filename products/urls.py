from django.urls import path
from . import views

urlpatterns = [
    path('products_one/', views.korean_foods, name='blog_one'),
    path('current_time/', views.date_time),
    path('products_three/', views.about_myself, name='about_myself'),

    path('', views.products, name='home_page'),
    path('products_list/<int:id>/', views.products_detail),
]
