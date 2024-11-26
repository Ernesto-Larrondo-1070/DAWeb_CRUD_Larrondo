from django.urls import path
from suplementos_app import views

urlpatterns = [
    path("suplemento", views.inicio_vistasSuplemento, name="suplemento"),
    path("registrarSuplemento/", views.registrarSuplemento, name="registrarSuplemento"),
    
    path("borrarSuplemento/<id_producto>", views.borrarSuplemento, name="borrarSuplemento"),
    path("seleccionarSuplemento/<id_producto>", views.seleccionarSuplemento, name="seleccionarSuplemento"),
    path("editarSuplemento/", views.editarSuplemento, name="editarSuplemento")
]