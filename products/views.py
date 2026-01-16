from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
        return HttpResponse('<img src="blob:https://web.telegram.org/e5ec8621-adf1-42bc-a6a0-b9211b005697"><p>Привет меня зовут Кайрат, мне 19 лет.')
