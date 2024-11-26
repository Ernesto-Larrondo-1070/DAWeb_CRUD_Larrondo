from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.

def inicio_vistasProveedor (request):
    losprov = Proveedor.objects.all()

    return render(request, "gestionarProveedor.html",{"misp": losprov})

def registrarProv(request):
    id_provee = request.POST["txtid"]
    num_ruta = request.POST["txtruta"]
    cant_prod = request.POST["txtcant"]
    peso  = request.POST["txtpeso"]
    tipo_prod = request.POST["txtipo"]
    direccion  = request.POST["txtdire"]

    guardarprov= Proveedor.objects.create(id_provee=id_provee, num_ruta = num_ruta, cant_prod=cant_prod, peso=peso, tipo_prod= tipo_prod, direccion = direccion)

    return redirect("/")

def borrarProv(request, id_provee):
    prov = Proveedor.objects.get(id_provee=id_provee)
    prov.delete()

    return redirect("/")

def seleccionarProv(request, id_provee):
    prov = Proveedor.objects.get(id_provee= id_provee)
    
    return render (request, "editarProveedor.html", {"misp":prov})

def editarProv(request):
    id_provee = request.POST["txtid"]
    num_ruta = request.POST["txtruta"]
    cant_prod = request.POST["txtcant"]
    peso  = request.POST["txtpeso"]
    tipo_prod = request.POST["txtipo"]
    direccion  = request.POST["txtdire"]

    
    prov = Proveedor.objects.get(id_provee=id_provee)

    prov.num_ruta = num_ruta
    prov.cant_prod = cant_prod
    prov.peso= peso
    prov.tipo_prod = tipo_prod
    prov.direccion = direccion
    prov.save()
    return redirect("/")