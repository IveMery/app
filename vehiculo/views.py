from django.shortcuts import render
from django.contrib import messages
from .forms import VehiculoForm,RegistroUsuarioForm
from tokenize import PseudoExtras
from django.contrib.auth import login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import VehiculoModel

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



#registro
def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type =ContentType.objects.get_for_model(VehiculoModel)
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo',content_type=content_type)
            user = form.save()
            user.user_permissions.add(visualizar_catalogo)
            login(request,user)
            messages.success(request, "Registrado Satisfactoriamente")
            return HttpResponseRedirect('/')

        messages.error(request, "Registro invalido.Algunos datos no son correctos")
    form = RegistroUsuarioForm()
    context = { "register_form" : form }
    return render(request, "registro.html", context)

#login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesion como : {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalido username o password")
        else:
             messages.error(request,"Invalido username o password")


    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)


def listar_vehiculo(request):
    vehiculos = VehiculoModel.objects.all()
    context = {'lista_vehiculos': vehiculos}
    print(vehiculos)
    print(request.user.get_all_permissions())
    return render(request, 'listar.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesion satisfactoriamente. ")
    return HttpResponseRedirect('/')
