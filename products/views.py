from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from products.models import Products



def products(request):
    if request.method == 'GET':
        products = Products.objects.all()
    return render(
        request,
        template_name='products/products_list.html',
        context={
            'products': products
        }
    )

def products_detail(request, id):

    if request.method == 'GET':
        products_id = get_object_or_404(Products, id=id)
    return render(
        request,
        template_name='products/products_detail.html',
        context={
            'products_id': products_id
        }
    )


def first_products(request):
    if request.method == 'GET':
        return HttpResponse("Кимчи, рис, кимпап, пулькоги, чачжанмен-топ 5 продуктов питания в Корее.")


def second_products(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(
            f"Дата: {now.strftime('%d.%m.%Y')}\n"
            f"Время: {now.strftime('%H:%M:%S')}" ,
        )


def third_products(request):
    if request.method == 'GET':
        return HttpResponse('<img src="blob:https://web.telegram.org/e5ec8621-adf1-42bc-a6a0-b9211b005697"><p>Привет меня зовут Кайрат, мне 19 лет.</p>')
