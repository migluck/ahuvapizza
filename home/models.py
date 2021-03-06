from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    """Home page model."""
    
    templates = "home/home_page.html"
    max_count = 1
    
    # Create new fields
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], null=True)
    banner_logo = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+"
        )
    banner_image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+"
        )
        
    content_panels = Page.content_panels + [
            MultiFieldPanel([
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_logo"),
                ImageChooserPanel("banner_image"),
            ], heading = "Banner Options")
        ]        
