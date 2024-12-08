from django.db import models
from datetime import datetime 
from django.utils.functional import cached_property
from django.urls.base import reverse

class LayoutModel(models.Model):
    layout_id = models.AutoField(primary_key=True)
    layout_domaine = models.CharField(max_length=1024,null=True, blank=True)
    layout_site_web = models.CharField(max_length=1024,null=True, blank=True)
    layout_site_web_url = models.CharField(max_length=1024,null=True, blank=True)
    layout_titre = models.CharField(max_length=1024,null=True, blank=True)
    layout_footer = models.CharField(max_length=1024,null=True, blank=True)
    
    description = models.TextField(max_length=1024,null=True, blank=True)
    image = models.CharField(max_length=1024,null=True, blank=True)
    lang = models.CharField(max_length=1024,null=True, blank=True)

    mentions_legales = models.CharField(max_length=1024,null=True, blank=True)
    mentions_legales_url = models.CharField(max_length=1024,null=True, blank=True)
  
    connexion = models.CharField(max_length=1024,null=True, blank=True)
    connexion_url = models.CharField(max_length=1024,null=True, blank=True)

    inscription = models.CharField(max_length=1024,null=True, blank=True)
    inscription_url = models.CharField(max_length=1024,null=True, blank=True)

    compte = models.CharField(max_length=1024,null=True, blank=True)
    compte_url = models.CharField(max_length=1024,null=True, blank=True)

    formulaire_parc = models.CharField(max_length=1024,null=True, blank=True)
    formulaire_parc_url = models.CharField(max_length=1024,null=True, blank=True)

    formulaire_manege = models.CharField(max_length=1024,null=True, blank=True)
    formulaire_manege_url = models.CharField(max_length=1024,null=True, blank=True)

    formulaire_restaurant = models.CharField(max_length=1024,null=True, blank=True)
    formulaire_restaurant_url = models.CharField(max_length=1024,null=True, blank=True)

    formulaire_hotel = models.CharField(max_length=1024,null=True, blank=True)
    formulaire_hotel_url = models.CharField(max_length=1024,null=True, blank=True)

    def __str__(self):
        return self.lang

    class Meta:
        verbose_name = 'layout'
       # indexes = [models.Index(fields=['lang'])]

class PageModel(models.Model):
    page_id = models.AutoField(primary_key=True)
    page = models.CharField(max_length=1024,null=True, blank=True)
    url = models.CharField(max_length=1024,null=True, blank=True)
    slug = models.CharField(max_length=1024,null=True, blank=True)
    template = models.CharField(max_length=1024,null=True, blank=True)
    image = models.CharField(max_length=1024,null=True, blank=True)
    lang = models.CharField(max_length=1024,null=True, blank=True)
    titre = models.CharField(max_length=200,null=True, blank=True)
    h1 = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    ancre1 = models.CharField(max_length=200,null=True, blank=True)
    ancre2 = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    date_update = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.page

    class Meta:
        verbose_name = 'page'
       # indexes = [models.Index(fields=['lang'])]
    
    #@cached_property
    #def url_frontend(self):
      #  return f"https://magicalcoaster.com{reverse('page_url', args=[self.lang, self.slug])}"


