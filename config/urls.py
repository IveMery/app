from django.contrib import admin
from django.urls import path, include
from vehiculo.views import indexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name= 'index'),
    path('vehiculo/', include('vehiculo.urls')),
]