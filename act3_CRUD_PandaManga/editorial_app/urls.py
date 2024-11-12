from django.urls import path
from editorial_app import views
urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarEditorial/",views.registrarEditorial,name="registrarEditorial"),
    path("seleccionarEditorial/<id_edit>",views.seleccionarEditorial,name="seleccionarEditorial"),
    path("editarEditorial/<id_edit>",views.editarEditorial,name="editarEditorial"),
    path("borrarEditorial/<id_edit>",views.borrarEditorial,name="borrarEditorial")
    
]