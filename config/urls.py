"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from notes import urls as notes_urls
from notes.api_urls import urlpatterns as notes_api_urls

urlpatterns = [
    path("", RedirectView.as_view(url="/notes/")),  # redirect to notes app
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("notes/", include(notes_urls)),
    path("api/", include(notes_api_urls)),
    path(
        "api-auth/", include("rest_framework.urls")
    ),  # for browsable API login # noqa: E501
]

urlpatterns += [
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # login/logout for views # noqa: E501
]
