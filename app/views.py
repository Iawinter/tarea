from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from requests import get

#def index(request):
#   return HttpResponse("Hello, Antonia Vega.")

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
    return render(request, 'app/templates/app/index.html', ciudades)