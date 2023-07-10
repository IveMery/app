from django.shortcuts import render
from django.contrib import messages
from .forms import VehiculoForm

def indexView(request):
    template_name = 'index.html'
    return render(request, template_name)


def addVehiculo(request):
    form = VehiculoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        form = VehiculoForm()
        messages.success(request, 'Los datos de han procesado exitosamente!')
    return render(request, "addform.html", {'form': form})    