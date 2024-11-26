from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def inicio_vistasCliente (request):
    losclientes = Cliente.objects.all()

    return render(request, "gestionarCliente.html",{"misclientes": losclientes})

def registrarCliente(request):
    id_cliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    num_tel = request.POST["numtel"]
    dire = request.POST["txtdire"]
    correo = request.POST["txtcorreo"]

    guardarcliente= Cliente.objects.create(id_cliente=id_cliente, nombre=nombre, apellido=apellido, num_tel=num_tel, dire=dire, correo=correo)

    return redirect("/")

def borrarCliente(request, id_cliente):
    cl = Cliente.objects.get(id_cliente=id_cliente)
    cl.delete()

    return redirect("/")

def seleccionarCliente(request, id_cliente):
    cl = Cliente.objects.get(id_cliente= id_cliente)
    
    return render (request, "editarCliente.html", {"misclientes":cl})

def editarCliente(request):
    id_cliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    num_tel = request.POST["numtel"]
    dire = request.POST["txtdire"]
    correo = request.POST["txtcorreo"]
    
    cls = Cliente.objects.get(id_cliente=id_cliente)

    cls.nombre= nombre
    cls.apellido = apellido
    cls.num_tel = num_tel
    cls.dire = dire
    cls.correo = correo
    cls.save()
    return redirect("/")