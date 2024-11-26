from django.shortcuts import render, redirect
from .models import Suplemento

# Create your views here.

def inicio_vistasSuplemento (request):
    lossupl= Suplemento.objects.all()

    return render(request, "gestionarSuplementos.html",{"misupl": lossupl})

def registrarSuplemento(request):
    id_producto = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    tipo = request.POST["txttipo"]
    sabor = request.POST["txtsabor"]
    precio_uni = request.POST["numprecio"]
    peso = request.POST["numpeso"]

    guardarproducto= Suplemento.objects.create(id_producto=id_producto, nombre=nombre,tipo=tipo, sabor=sabor, precio_uni=precio_uni, peso=peso)

    return redirect("/")

def borrarSuplemento(request, id_producto):
    supl = Suplemento.objects.get(id_producto=id_producto)
    supl.delete()

    return redirect("/")

def seleccionarSuplemento(request, id_producto):
    supl = Suplemento.objects.get(id_producto= id_producto)
    
    return render (request, "editarSuplementos.html", {"misupl":supl})

def editarSuplemento(request):
    id_producto = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    tipo = request.POST["txttipo"]
    sabor = request.POST["txtsabor"]
    precio_uni = request.POST["numprecio"]
    peso = request.POST["numpeso"]
    
    supl = Suplemento.objects.get(id_producto=id_producto)

    supl.nombre= nombre
    supl.sabor = sabor
    supl.tipo = tipo
    supl.precio_uni = precio_uni
    supl.peso = peso
    supl.save()
    return redirect("/")