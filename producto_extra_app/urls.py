from django.urls import path
from producto_extra_app import views

urlpatterns = [
    path("producto_extra", views.inicio_vistasProducto_extra, name="producto_extra"),
    path("registrarProd/", views.registrarProd, name="registrarProd"),
    
    path("borrarProd/<id_prod>", views.borrarProd, name="borrarProd"),
    path("seleccionarProd/<id_prod>", views.seleccionarProd, name="seleccionarProd"),
    path("editarProd/", views.editarProd, name="editarProd")
]