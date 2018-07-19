from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.db.models import Q
from .models import Image
from .forms import (ImageEditForm, ImageUploadForm)
_lr = loader.render_to_string


def index(req):
    qs = req.GET.get('q')
    if qs:
        qs = qs.replace(' ', '')  # spaces removal
        rows = set(Image.objects.filter(Q(title__icontains=qs) | Q(tags__name__icontains=qs)))
        ttl = f'поиск по заголовкам и тегам фразы: {qs}'
    else:
        rows = Image.objects.filter(active=True).defer('active')[:200]
        qs = ''
        ttl = 'все изображения'
    res = _lr('index.html', {
        'title': ttl,
        'rows': rows,
        'qs': qs
    }, req)

    return HttpResponse(res)


def img_add(req):
    # добавление изображения
    if req.method == 'POST':
        form = ImageUploadForm(data=req.POST, files=req.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(req, 'Новое изображение загружено')
        else:
            messages.error(req, 'Ошибка при загрузке')
        return HttpResponseRedirect("/")
    else:
        ctx = {'title': 'загрузка нового изображения', 'form': ImageUploadForm()}
        return HttpResponse(_lr('img_add.html', ctx, req))


def img_view(req, slug):
    # простотр редактировние описаний
    try:
        img = Image.objects.get(slug__exact=slug)
    except Exception:
        raise Http404('Don\'t exists')

    if req.method == 'POST':
        form = ImageEditForm(instance=img, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'описание обновлено')
        else:
            messages.error(req, 'Ошибка при обновлении')
        return HttpResponseRedirect("/")
    else:
        ctx = {'title': 'изображение', 'form': ImageEditForm(instance=img), 'id': img.id, 'iurl': img.image.url}
        return HttpResponse(_lr('img_view.html', ctx, req))


def img_del(req, id):
    # удаление изображения
    try:
        # удаление файла на диске можно добавть тут
        Image.objects.filter(id=id).delete()
        messages.success(req, 'изображение удалено')
        return HttpResponseRedirect("/")
    except Exception:
        messages.error(req, 'Ошибка при удалении')
