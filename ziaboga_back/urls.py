"""ziaboga_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from data_manager import views
from data_manager.views import ErabiltzaileaViewSet,EgutegiaViewSet,GlobalaViewSet,TaldeakViewSet

router = routers.DefaultRouter()
router.register(r'erabiltzailea', ErabiltzaileaViewSet)
router.register(r'egutegia', EgutegiaViewSet)
router.register(r'globala', GlobalaViewSet)
router.register(r'taldea', TaldeakViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('datuak/', views.datuak_apiView, name="datuak"),
    path('erregistratu/', views.erregistratu_apiView, name="erregistratu"),
    path('erabiltzaileaEgiaztatu/', views.erabiltzaileaEgiaztatu_apiView, name="erabiltzaileaEgiaztatu"),
    path('gremiokoAurkariak/', views.gremiokoAurkariak_apiView, name="gremiokoAurkariak"),
    path('kinielaBete/', views.kinielaBete_apiView, name="kinielaBete"),
    path('kinielaJaso/', views.kinielaJaso_apiView, name="kinielaJaso"),
    path('taldeakJaso/', views.taldeakJaso_apiView, name="taldeakJaso"),
    path('estropadakoEmaitza/', views.estropadakoEmaitza_apiView, name="estropadakoEmaitza"),
    path('gremioaSortu/', views.gremioaSortu_apiView, name="gremioaSortu"),
    path('gremioanSartu/', views.gremioanSartu_apiView, name="gremioanSartu"),
    path('egutegia/', EgutegiaViewSet.as_view, name="egutegia"),
    path('globala/', GlobalaViewSet.as_view, name="globala"),
    path('taldea/', TaldeakViewSet.as_view, name="taldea")
]
