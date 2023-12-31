"""Django_DRF_Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Student, name='Student')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='Student')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student import views
from Student import view_drf

urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentinfo/<int:pk>", views.student_details),
    path("studentlist/", views.student_list),
    path("student_create/", views.student_create),
    path("studentdata/", view_drf.student_api)
]
