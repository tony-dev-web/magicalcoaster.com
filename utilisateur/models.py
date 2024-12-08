from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns
from datetime import datetime
from django.utils.functional import cached_property
from django.urls.base import reverse



class UtilisateurModel(DjangoCassandraModel):
    utilisateur_id = columns.Integer(primary_key=True)
    url = columns.Text()
    utilisateur = columns.Text()
    slug = columns.Text()
    vues = columns.Integer(default=0)
    lang = columns.Text()
    titre = columns.Text()
    description = columns.Text()
    groupe = columns.Text()
    #date_creation = columns.DateTime(default=datetime.now)
    date = columns.Text(default=datetime.now().strftime("%d-%m-%Y %H:%M"))
    certifier = columns.Integer(default=0)
    session = columns.Text()
    email = columns.Text()
    
    adresse  = columns.Text()
    ville = columns.Text()
    departement = columns.Text()
    region = columns.Text()
    pays = columns.Text()
    code_postale = columns.Text()
    site_web = columns.Text()
    domaine = columns.Text()
    telephone = columns.Text()

    parc_prefere = columns.Text()
    manege_prefere = columns.Text()
    coaster_prefere = columns.Text()
    hotel_prefere = columns.Text()
    land_prefere = columns.Text()
    spectacle_prefere = columns.Text()
    boutique_prefere = columns.Text()
    restaurant_prefere = columns.Text()
    
    photo = columns.Text()
    photo_alt = columns.Text()
    photo_favicon = columns.Text()
    
    ranking = columns.Integer(default=0)
    ranking_score = columns.Integer(default=0)

    valide = columns.Integer(default=1)

    def __str__(self):
        return self.utilisateur
    
    class Meta:
        verbose_name = 'Utilisateur'
   
    @cached_property
    def url_frontend(self):
        return f"https://magicalcoaster.com{reverse('utilisateur_url', args=[self.lang, self.slug])}"