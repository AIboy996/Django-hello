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
    path('model/more_query/', database.more_query),
    path('model/update/', database.update),
    path('model/delete/', database.delete),
    path('search-form/', views.search_form),
    path('search/', views.search),
    path('search-post/', views.search_post),
    path('request-info/', views.info),
    # 20011021
    re_path(r'^re_match/(?P<year>[0-9]{4})(?P<month>[0-9]{2})(?P<day>[0-9]{2})/$', views.re_match)
]
