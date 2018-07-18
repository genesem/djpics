# fields reference
# https://docs.djangoproject.com/en/2.0/ref/models/fields/


from django.db import models

class Page(models.Model):
    class Meta:
        db_table = 't_page'

    name = models.CharField(max_length=60, blank=True, db_index=True)
    slug = models.CharField(max_length=60, blank=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    text = models.TextField(default=" Some text goes here, just for example ")

    def __str__(self):
        return self.name
