"""HospMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from hospital.views import *

#name parameter is used for 'url' in Django Template Language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('contact/', contact),
    path('', index),
    path('admin_login/', Login),
    path('logout/', Logout),
    path('view_doctor/', view_doctor),
    path('add_doctor/', add_doctor),
    path('delete_doctor/<int:pid>/', delete_doctor),
    path('edit_doctor/<int:pid>/', edit_doctor),
    path('view_patient/', view_patient),
    path('add_patient/', add_patient),
    path('delete_patient/<int:pid>/', delete_patient),
    path('edit_patient/<int:pid>/', edit_patient),
    path('view_appointment/', view_appointment),
    path('add_appointment/', add_appointment),
    path('delete_appointment/<int:pid>/', delete_appointment),
    path('edit_appointment/<int:pid>/', edit_appointment),
    path('view_medicine/', view_medicine),
    path('add_medicine/', add_medicine),
    path('delete_medicine/<int:pid>/', delete_medicine),
    path('edit_medicine/<int:pid>/', edit_medicine),
]
