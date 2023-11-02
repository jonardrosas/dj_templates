from django.db import models

from wagtail.models import Page
from rest_framework.serializers import Field
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from core.api.serializer import CommonPageSerializer

from wagtail.api import APIField


class HomePage(Page):
    header = models.CharField(max_length=192, blank=True)
    subtitle = models.CharField(max_length=192, blank=True)
    text = models.CharField(max_length=192, blank=True)
    cta = models.CharField(max_length=192, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("header"),
    ]

    api_fields = [
        APIField("header"),
    ]
