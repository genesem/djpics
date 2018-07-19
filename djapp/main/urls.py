
from django.urls.conf import path  # re_path, include,
from django.contrib.admin.sites import site

from django.views.generic.base import TemplateView  # this is used for static_pages inside your django app

from django.conf import settings
from django.conf.urls.static import static

from .views import (index, page)

urlpatterns = [
    path('a/admin/', site.urls),  # admin.site.urls
    path('a/', TemplateView.as_view(template_name='static_pages/index.html', extra_context={'title': 'this is django rendered static page'})),
    path('', index, name='idx'),
    path('p/index/', index, name='index'),
    path('p/page/', page, name='page')
]

# не для production, в prod. для статики исп nginx front
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
