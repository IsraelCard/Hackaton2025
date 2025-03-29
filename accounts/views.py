from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Importar AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import DispositivoForm
from .models import Dispositivo

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Usar AuthenticationForm
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()  # Usar AuthenticationForm
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    dispositivos = Dispositivo.objects.filter(usuario=request.user)
    activos = dispositivos.filter(estado=True).count()
    inactivos = dispositivos.filter(estado=False).count()
    
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            dispositivo = form.save(commit=False)
            dispositivo.usuario = request.user
            dispositivo.save()
            return redirect('home')
    else:
        form = DispositivoForm()
    
    return render(request, 'home.html', {
        'dispositivos': dispositivos,
        'form': form,
        'activos': activos,
        'inactivos': inactivos
    })

@login_required
def eliminar_dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
    dispositivo.delete()
    return redirect('home')

@login_required
def toggle_device(request, device_id):
    if request.method == 'POST':
        dispositivo = Dispositivo.objects.get(id=device_id, usuario=request.user)
        dispositivo.estado = not dispositivo.estado
        dispositivo.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@login_required
def dispositivo_detalle(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
    data = {
        'id': dispositivo.id,
        'nombre': dispositivo.nombre,
        'tipo': dispositivo.get_tipo_display(),
        'estado': 'Activo' if dispositivo.estado else 'Inactivo',
        'consumo': dispositivo.consumo,
        'descripcion': dispositivo.descripcion,
        'ubicacion': dispositivo.ubicacion,
        'ip_address': dispositivo.ip_address,
        'fecha_creacion': dispositivo.fecha_creacion.strftime("%d/%m/%Y %H:%M"),
        'ultima_actualizacion': dispositivo.ultima_actualizacion.strftime("%d/%m/%Y %H:%M"),
    }
    return JsonResponse(data)

@login_required
def chart_view(request):
    data = {
        "labels": ["Enero", "Febrero", "Marzo", "Abril"],
        "values": [10, 20, 30, 40],
    }
    return render(request, "calculadora.html", {"data": data})
