from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from requests import get

def index(request):
    ciudades= {"cities": []}
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/cities")
    r = r.json()
    print(r)
    lista = []
    for ep1 in r:
        if ep1["name"] not in lista:
            lista.append(ep1["name"])
    ciudades["cities"] = lista
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/users")
    r = r.json()
    lista = []
    for ep in r:
        if ep["name"] not in lista:
            lista.append(ep["name"])
    ciudades["usuarios"] = lista
    return render(request, 'index.html', ciudades)

def ciudades(request, id_ciudad):
    dicc = {'nombre': [], 'pais': [], 'usuarios': []}
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/cities")
    r = r.json()
    lista = []
    lista1 = []
    lista2 = []
    for ci in r:
        if ci["name"] == id_ciudad:
            lista.append(ci["name"])
            lista1.append(ci["country"])
            lista2.append(ci["users"])
    dicc["nombre"] = lista[0]
    dicc["pais"] = lista1[0]
    dicc["usuarios"] = lista2[0]
    return render(request, 'ciudades.html', dicc)
