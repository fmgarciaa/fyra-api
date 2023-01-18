"""Main Urls module"""

# Django
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    # Fyra's urls
    path('', include(('fyra.users.urls', 'users'), namespace='users')),
    path('', include(('fyra.products.urls', 'units'), namespace='units')),
    path('', include(('fyra.products.urls', 'categories'), namespace='categories')),
    path('', include(('fyra.products.urls', 'products'), namespace='products')),
    path('', include(('fyra.customers.urls', 'customers'), namespace='customers')),
    path('', include(('fyra.orders.urls', 'orders'), namespace='orders')),
    path('', include(('fyra.reports.urls', 'reports'), namespace='reports')),
    path('', include(('fyra.reports.urls', 'stats'), namespace='stats')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
