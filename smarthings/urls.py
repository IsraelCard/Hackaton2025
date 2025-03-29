from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('eliminar-dispositivo/<int:dispositivo_id>/', views.eliminar_dispositivo, name='eliminar_dispositivo'),
    path('toggle-device/<int:device_id>/', views.toggle_device, name='toggle_device'),
    path('dispositivo/<int:dispositivo_id>/', views.dispositivo_detalle, name='dispositivo_detalle'),
    path('calculadora/', views.chart_view, name='chart'),
]