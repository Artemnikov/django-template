from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include
from django.views.decorators.csrf import get_token

router = routers.SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]
urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)