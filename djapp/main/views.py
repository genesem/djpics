from django.template import loader
from django.http import HttpResponse, Http404
from .models import Page
_lr = loader.render_to_string


def index(req):
    try:
        pg = Page.objects.get(slug__exact='index')
    except Page.DoesNotExist:
        raise Http404('Page don\'t exists')
    ctx = {
        'title': 'index title',
        'pg': pg,
    }
    return HttpResponse(_lr('index.html', ctx, req))


def page(req):
    try:
        pg = Page.objects.get(slug__exact='page')
    except Page.DoesNotExist:
        raise Http404('Page don\'t exists')
    ctx = {
        'title': 'page title',
        'pg': pg,
    }
    return HttpResponse(_lr('page.html', ctx, req))
