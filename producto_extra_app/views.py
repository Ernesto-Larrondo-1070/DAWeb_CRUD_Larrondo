from django.shortcuts import render, redirect
from .models import Producto_extra

# Create your views here.

def inicio_vistasProducto_extra (request):
    losprod= Producto_extra.objects.all()

    return render(request, "gestionarProd.html",{"misprod": losprod})

def registrarProd(request):
    id_prod = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    tipo = request.POST["txttipo"]
    talla = request.POST["txtalla"]
    precio_uni = request.POST["numprecio"]
    peso = request.POST["numpeso"]
    id_proveedor = request.POST["txtidprov"]

    guardarproducto= Producto_extra.objects.create(id_prod=id_prod, nombre=nombre,tipo=tipo, talla=talla, precio_uni=precio_uni, peso=peso, id_proveedor=id_proveedor)

    return redirect("/")

def borrarProd(request, id_prod):
    prod_extra = Producto_extra.objects.get(id_prod=id_prod)
    prod_extra.delete()

    return redirect("/")

def seleccionarProd(request, id_prod):
    prod_extra = Producto_extra.objects.get(id_prod= id_prod)
    
    return render (request, "editarProd.html", {"misprod":prod_extra})

def editarProd(request):
    id_prod = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    tipo = request.POST["txttipo"]
    talla = request.POST["txtalla"]
    precio_uni = request.POST["numprecio"]
    peso = request.POST["numpeso"]
    id_proveedor = request.POST["txtidprov"]
    
    prod_extra = Producto_extra.objects.get(id_prod=id_prod)

    prod_extra.nombre= nombre
    prod_extra.talla = talla
    prod_extra.tipo = tipo
    prod_extra.precio_uni = precio_uni
    prod_extra.peso = peso
    prod_extra.id_proveedor = id_proveedor
    prod_extra.save()
    return redirect("/")