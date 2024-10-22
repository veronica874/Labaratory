"""
URL configuration for labaratory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from computer.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='login'),
    path('home_list/',home_view,name='home'),
    path('labaratory_list/',labaratory_view,name='labaratory'),
    path('lab_attendant_list/',lab_attendant_view,name='attendant'),
    path('computers_list/',computers_view,name='computer'),
    
  
]
