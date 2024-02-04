"""
URL configuration for fablab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from fablab_backend import views
from django.shortcuts import render
from datetime import date, datetime

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.GET_fablab_worktypes, name='fablab_worktypes'),
    path("delete_view_fablab/<int:process_id>/", views.delete_view_fablab, name='delete_view_fablab'),
    path("view_fablab/<int:process_id>/", views.view_fablab, name='view_fablab'),
]