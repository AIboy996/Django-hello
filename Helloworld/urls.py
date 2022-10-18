"""Helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from . import views, database


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.hello), 
    path('text/', views.text),
    path('child/', views.child),
    path('model/', database.model),
    path('model/add/', database.adddata),
    path('model/query/', database.query),
    path('model/update/', database.update),
    path('model/delete/', database.delete),
    path('search-form/', views.search_form),
    path('search/', views.search),
    path('search-post/', views.search_post),
    path('request-info/', views.info)
]
