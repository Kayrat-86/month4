from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from .models import Basket

def add_to_basket(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if request.method == 'POST':
        Basket.objects.create(
            product=product,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            quantity=request.POST.get('quantity')
        )
        return redirect('basket_list')

    return render(request, 'basket/add_to_basket.html', {'product': product})


def basket_list(request):
    baskets = Basket.objects.filter(is_ordered=False)
    return render(request, 'basket/basket_list.html', {'baskets': baskets})


def delete_from_basket(request, id):
    basket = get_object_or_404(Basket, id=id)
    basket.delete()
    return redirect('basket_list')


def edit_order(request, id):
    basket = get_object_or_404(Basket, id=id)

    if request.method == 'POST':
        basket.full_name = request.POST.get('full_name')
        basket.phone = request.POST.get('phone')
        basket.address = request.POST.get('address')
        basket.quantity = request.POST.get('quantity')
        basket.save()
        return redirect('basket_list')

    return render(request, 'basket/edit_order.html', {'basket': basket})
