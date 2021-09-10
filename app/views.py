from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from requests import get

def index(request):
    ciudades= {"cities": []}
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/cities")
    r = r.json()
    lista = []
    for ep1 in r:
        if ep1["name"] not in lista:
            lista.append(ep1["name"])
    ciudades["cities"] = lista
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/users")
    r = r.json()
    lista = []
    lista2 = []
    for ep in r:
        if ep["name"] not in lista:
            a = ep["name"] + " " + ep["lastName"]
            lista.append(a)
    ciudades["usuarios"] = lista
    ciudades["ides"] = lista2
    return render(request, 'index.html', ciudades)

def ciudades(request, id_ciudad):
    dicc = {'nombre': [], 'pais': [], 'usuarios': []}
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/cities")
    r = r.json()
    lista = []
    lista1 = []
    lista2 = []
    listaf = []
    for ci in r:
        if ci["name"] == id_ciudad:
            lista.append(ci["name"])
            lista1.append(ci["country"])
            lista2.append(ci["users"])
    dicc["nombre"] = lista[0]
    dicc["pais"] = lista1[0]
    for us in lista2[0]:
        j = get(f"https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/users/{us}")
        j = j.json()
        a = j["name"] +" "+ j["lastName"]
        listaf.append(a)
    dicc["usuarios"] = listaf
    return render(request, 'ciudades.html', dicc)

def usuarios(request, id_usuario):
    r = get("https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/users")
    r = r.json()
    a = id_usuario
    a = a.replace("%20", " ")
    z = a #nombre y apellido
    a, b = a.split(sep=" ")
    for user in r:
        if user["name"] == a and user["lastName"] == b:
            c = user["id"]
            i = get(f"https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/users/{c}/credit-cards")
            i = i.json()
            lista = []
            for te in i:
                y = te["CVV"]
                y = str(y)
                g = te["creditCard"]
                g = str(g)
                f = g + " /  CVV:" + y
                if f not in lista:
                    lista.append(f)
            j = get(f"https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26425/users/{c}/addresses")
            j = j.json()
            lista2 = []
            for ad in j:
                if ad["address"] not in lista:
                    lista2.append(ad["address"])
            diccionario = {'nombre': z, 'foto': user['avatar'], 'mail': user['email'], 'credito': lista,
                           "direcciones": lista2}
    return render(request, 'usuarios.html', diccionario)