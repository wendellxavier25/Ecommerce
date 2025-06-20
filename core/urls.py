from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns = [
        # TODO: remover
        path('__debug__/', include('debug_toolbar.urls')),

    ] + urlpatterns