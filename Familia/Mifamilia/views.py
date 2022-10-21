from django.http import HttpResponse
from django.shortcuts import render
from .models import  Nombres


def nombres(request,nombre,Dni,nacimiento):

    datos = Nombres(nombre=nombre, Dni=Dni, nacimiento=nacimiento)
    datos.save()

    return HttpResponse(f"""
        <p>Nombre: {datos.nombre} - con dni: {datos.Dni} y nacio en el {datos.nacimiento} agregado! </p>
    """)


def lista_familias(request):

    lista = Nombres.objects.all()

    return render(request, "familia.html", {"lista_familias":lista})