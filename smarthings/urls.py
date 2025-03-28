from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.login_view, name='login'),
    path('register/', accounts_views.register, name='register'),
    path('home/', accounts_views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]