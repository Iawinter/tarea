from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from requests import get

#def index(request):
#   return HttpResponse("Hello, Antonia Vega.")

def index(request):
    ciudades= {"cities": [], "usuarios": []}
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/cities")
    r = r.json()
    lista = []
    for ep1 in r:
        if ep1["name"] not in lista:
            lista.append(ep1["name"])
    ciudades["cities"] = lista
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/usuarios")
    r = r.json()
    lista = []
    for ep in r:
        if ep["name"] not in lista:
            lista.append(ep["name"])
    ciudades["usuarios"] = lista
    return render(request, 'aplicacion/index.html', ciudades)