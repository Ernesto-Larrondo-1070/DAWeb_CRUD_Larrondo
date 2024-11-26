from django.shortcuts import render, redirect
from .models import Venta

# Create your views here.

def inicio_vistasVenta (request):
    lasventas = Venta.objects.all()

    return render(request, "gestionarVentas.html",{"misv": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtid"]
    cliente = request.POST["txtidcl"]
    id_prod = request.POST["txtidprod"]
    precio  = request.POST["txtprecio"]
    cantidad = request.POST["txtcantidad"]
    gr_kg = request.POST["txtgr"]
    servicios = request.POST["txtserv"]


    guardarventa= Venta.objects.create(cliente=cliente, id_venta = id_venta, id_prod=id_prod, precio=precio, cantidad= cantidad,gr_kg = gr_kg, servicios=servicios)

    return redirect("/")

def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()

    return redirect("/")

def seleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta= id_venta)
    
    return render (request, "editarVentas.html", {"misv":venta})

def editarVenta(request):
    id_venta = request.POST["txtid"]
    cliente = request.POST["txtidcl"]
    id_prod = request.POST["txtidprod"]
    precio  = request.POST["txtprecio"]
    cantidad = request.POST["txtcantidad"]
    gr_kg = request.POST["txtgr"]
    servicios = request.POST["txtserv"]

    
    venta = Venta.objects.get(id_venta=id_venta)

    venta.cliente = cliente
    venta.id_prod = id_prod
    venta.precio= precio
    venta.cantidad = cantidad
    venta.gr_kg = gr_kg
    venta.servicios = servicios
    venta.save()
    return redirect("/")