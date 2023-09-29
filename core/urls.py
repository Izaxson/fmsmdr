import statistics
from django.contrib import admin
from django.urls import include, path

from core import settings

urlpatterns = [
    # path('admin/defender/', include('defender.urls')), # defender admin
    path('admin/', admin.site.urls),
    path('', include('fms.urls')),
    path('', include('account.urls'))
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

