"""
URL configuration for boilerplate project.

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

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import CustomReleaseUserView, infoView

urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("admin/", admin.site.urls),
    path("hijack/release/", CustomReleaseUserView.as_view(), name="release"),
    path("hijack/", include("hijack.urls")),
    path("", include("polls.urls")),
    path("cbvpolls/", include("cbvpolls.urls")),
    path("info", infoView, name="info"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()
