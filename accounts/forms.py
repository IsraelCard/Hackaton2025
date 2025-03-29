from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Dispositivo

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nombre', 'tipo', 'descripcion', 'ubicacion', 'ip_address','consumo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'consumo': forms.NumberInput(attrs={'class': 'form-control'})
        }
class RegistroForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Las contraseñas no coinciden.',
        'password_too_short': 'La contraseña debe contener al menos %(min_length)d caracteres.',
        'password_common': 'Esta contraseña es demasiado común.',
        'password_entirely_numeric': 'La contraseña no puede ser completamente numérica.',
    }
            
