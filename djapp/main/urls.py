# your site URL Configuration
# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/2.0/topics/http/urls/
# Examples:
# Function views
#    1. Add an import:  from my_app import views
#    2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#    1. Add an import:  from other_app.views import Home
#    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#    1. Import the include() function: from django.urls import include, path
#    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


from django.urls import path
from django.contrib import admin
from django.views.generic.base import TemplateView  # this is used for static_pages inside your django app

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('a/admin/', admin.site.urls),
    path('a/', TemplateView.as_view(template_name='static_pages/index.html', extra_context={'title': 'this is django rendered static page'})),
    path('', index, name='idx'),
    path('p/index/', index, name='index'),
    path('p/page/', page, name='page')
] 

# не для продакшн, в прод. исп nginx front server
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

