from django.contrib import admin
from django.urls import path
from contato.views import index, detalhar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("detalhar/<int:id>", detalhar, name="detalhar"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)