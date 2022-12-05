from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # ----Django
    path("admin/", admin.site.urls),

    #(r'^i18n/', include('django.conf.urls.i18n')),

    # ----Project
    re_path(r'^', include('main.urls')),
    re_path(r'^common/', include('common.urls')),
    re_path(r'^inventory/', include('inventory.urls')),
    re_path(r'^assets/', include('assets.urls')),
    re_path(r'^search/', include('dynamic_search.urls')),
    #re_path(r'^import/', include('importer.urls')),
    re_path(r'^movements/', include('movements.urls')),
    re_path(r'^generic_photos/', include('photos.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += [
            re_path(r'^rosetta/', include('rosetta.urls'), name='rosetta'),
        ]
