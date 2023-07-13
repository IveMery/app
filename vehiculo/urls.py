from django.urls import path
from .views import *

urlpatterns = [ 
    path('', indexView, name = 'index'),
    path('add/',addVehiculo , name = 'addform'),
    path('listar/',listarView , name ='listar'),
    path('registro/',registro_view,name="registro"),
    path('login/', login_view, name="login"),
    path('listar/', listar_vehiculo, name = 'listar'),
]

