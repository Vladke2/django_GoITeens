from django.shortcuts import render, HttpResponse


def name(request):
    return HttpResponse("Ім'я: Влад Прізвище: Січкар ")


def age(request):
    return HttpResponse('Вік: 16')


def hobby(request):
    return HttpResponse('Відпочинок')
