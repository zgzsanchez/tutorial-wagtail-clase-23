from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel





class HomePage(Page):
    '''
    Añadimos campo *body* de texto enriquecido
    '''
    # subpage de la apñlicación blog
    #subpage_types = ['blog.BlogIndexPage']

    # no permito que tenga nuevas subpáginas
    subpage_types = []

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),

    ]


