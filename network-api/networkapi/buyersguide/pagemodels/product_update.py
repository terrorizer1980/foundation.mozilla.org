from django.db import models

from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from wagtail.search import index


@register_snippet
class Update(index.Indexed, models.Model):
    # TODO: We need to migrate this to the wagtailpages app.
    # TODO: There needs to be a data migration included.
    source = models.URLField(
        max_length=2048,
        help_text='Link to source',
    )

    title = models.CharField(
        max_length=256,
    )

    author = models.CharField(
        max_length=256,
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
        help_text='feature this update at the top of the list?'
    )

    snippet = models.TextField(
        max_length=5000,
        blank=True,
    )

    created_date = models.DateField(
        auto_now_add=True,
        help_text='The date this product was created',
    )

    panels = [
        FieldPanel('source'),
        FieldPanel('title'),
        FieldPanel('author'),
        FieldPanel('featured'),
        FieldPanel('snippet'),
    ]

    search_fields = [
        index.SearchField('title', partial_match=True),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Buyers Guide Product Update"
        verbose_name_plural = "Buyers Guide Product Updates"
