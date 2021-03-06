# -*- coding: utf-8 -*-
"""koldunov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from koldunov.api.views.auth_views import Login, logout
from koldunov.api.views.schema import schema_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/auth/login/', Login.as_view(), name="login"),
    url(r'^app/auth/logout/', logout, name="logout"),
    url(r'^app/api/', include('koldunov.api.urls')),
    url(r'^schema/$', schema_view),
]
