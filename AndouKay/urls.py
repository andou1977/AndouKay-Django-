"""AndouKay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from rest_framework import routers

from AndouKay import settings
from Andou_Kay import views

router = routers.DefaultRouter()
router.register('ouestapi', views.OuestView)
#router.register('ju', views.idone)


urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('', include(router.urls)),
    path("listerbyidouest/<int:pk>/", views.litbyidouest, name="listerbyidouest"),
    path("listerbyidouest/", views.listouestforid, name="idouest"),
    path('ouest/', views.ouest, name='ouest'),
    path('searchquest/', views.searchquest, name='searchquest'),
    path('pageerror/', views.pageerror, name='pageerror'),
    path('view/', views.view, name='view'),
    path('sud/', views.sud, name='sud'),
    path('searchsud/', views.searchsud, name='searchsud'),
    path('nord/', views.nord, name='nord'),
    path('searchnord/', views.searchnord, name='searchnords'),
    path('nippes/', views.nippes, name='nippes'),
    path('searcnippes/', views.searcnippes, name='searcnippes'),
    path('idouest/<int:id>/', views.idouest, name='idouest'),


    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

