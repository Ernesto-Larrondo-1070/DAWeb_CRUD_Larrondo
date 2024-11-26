from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def inicio_vistasEmpledo (request):
    losempleado = Empleado.objects.all()

    return render(request, "gestionarEmpleado.html",{"misem": losempleado})

def registrarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    rfc = request.POST["txtrfc"]
    curp = request.POST["txtcurp"]
    num_tel = request.POST["numtel"]
    dire = request.POST["txtdire"]
    sexo = request.POST["txtsex"]

    guardarempleado= Empleado.objects.create(id_empleado=id_empleado, nombre=nombre, apellido=apellido, num_tel=num_tel, dire=dire, rfc=rfc, curp=curp,sexo=sexo)

    return redirect("/")

def borrarEmpleado(request, id_empleado):
    em = Empleado.objects.get(id_empleado=id_empleado)
    em.delete()

    return redirect("/")

def seleccionarEmpleado(request, id_empleado):
    em = Empleado.objects.get(id_empleado=id_empleado)
    
    return render (request, "editarEmpleado.html", {"misem":em})


def editarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    rfc = request.POST["txtrfc"]
    curp = request.POST["txtcurp"]
    num_tel = request.POST["numtel"]
    dire = request.POST["txtdire"]
    sexo = request.POST["txtsex"]
    em = Empleado.objects.get(id_empleado=id_empleado)
    em.nombre = nombre
    em.apellido = apellido
    em.rfc = rfc
    em.curp = curp
    em.num_tel = num_tel
    em.dire = dire
    em.sexo = sexo
    em.save()
    return redirect("/") 