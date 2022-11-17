from django.conf.urls import include
try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import url
from django.contrib.auth import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
urlpatterns = [
    # Example:
    # url(r'^idptest/', include('idptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),

    # Required for login:
    url(r'^accounts/login/$', login),

    # URLs for the IDP:
    url(r'^idp/', include('saml2idp.urls')),
]
