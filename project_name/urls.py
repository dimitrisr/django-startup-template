from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static

from .app.hello_world.views import hello

admin.site.site_header = '{{ project_name }}'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = [
    # Admin panel and documentation:
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    re_path(r'^admin/', admin.site.urls),

    # make sure you delete this entry
    re_path(r'^/?$', hello)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)