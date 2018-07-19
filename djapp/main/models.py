from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from datetime import date
import itertools
from re import sub


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
    class Meta:
        db_table = 't_img'

    active = models.BooleanField(default=True, db_index=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    image = models.ImageField(upload_to='images/%Y-%m/%d')
    desc = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    shooted = models.DateField(default=date.today)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # self.title = sub('[^\w ]+', '', self.title.strip())[:200]
        if not self.slug:
            self.slug = orig = 'img' + slugify(self.title[:180])

            # генерация уник slug
            for x in itertools.count(1):
                if not Image.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (orig, x)

        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
