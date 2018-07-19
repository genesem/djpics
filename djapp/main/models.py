from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from re import sub


class Page(models.Model):
    class Meta:
        db_table = 't_page'

    name = models.CharField(max_length=60, blank=True, db_index=True)
    slug = models.CharField(max_length=60, blank=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    text = models.TextField(default="Some text, just for example")

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        db_table = 't_tag'

    name = models.CharField(max_length=40)
    slug = models.CharField(editable=True, blank=True, max_length=40, db_index=True, unique=True)
    slen = models.PositiveSmallIntegerField(default=0, editable=False, db_index=True)

    def save(self, **kwargs):
        self.name = sub('[^\w ]+', '', self.name.strip())[:40]
        if not self.slug:
            self.slug = slugify(self.name)
        self.slen = len(self.slug)
        super(Tag, self).save()

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y-%m/%d')
    desc = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = sub('[^\w ]+', '', self.title.strip())[:200]
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
