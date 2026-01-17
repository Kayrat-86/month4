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




def korean_foods(request):
    if request.method == 'GET':
        return HttpResponse("Кимчи, рис, кимпап, пулькоги, чачжанмен-топ 5 продуктов питания в Корее.")


def date_time(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(
            f"Дата: {now.strftime('%d.%m.%Y')}\n"
            f"Время: {now.strftime('%H:%M:%S')}" ,
        )


def about_myself(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://st4.depositphotos.com/3881799/27242/i/450/depositphotos_272424264-stock-photo-hacker-working-laptop-dark.jpg"><p>Привет меня зовут Кайрат, мне 19 лет.</p>')
