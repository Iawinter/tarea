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
    r = get(f"https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/cities/{id_ciudad}")
    r = r.json()
    #r = r[0]
    diccionario = {'nombre': r['name'], 'pais': r['country'], 'usuarios': r['users']}
    return render(request, 'ciudades.html', diccionario)
