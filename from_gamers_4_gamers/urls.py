"""
URL configuration for from_gamers_4_gamers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from_gamers_4_gamers/urls.py
from django.contrib import admin
from django.urls import path, include
from store.views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('products/', views.product_list, name='products'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth-related URLs

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
