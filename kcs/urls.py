from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/login', views.LoginView.as_view(), name='login'),
    path('users/', include('django.contrib.auth.urls')),
]
