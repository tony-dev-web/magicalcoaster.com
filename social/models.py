from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns
from datetime import datetime
#liste de parc visité 
#liste des manege effectué

class SocialModel(DjangoCassandraModel):
    social_id = columns.Text(primary_key=True)
    utilisateur_id = columns.Integer(index=True)
    utilisateur_url = columns.Text()
    utilisateur = columns.Text()
    vues = columns.Integer(default=0)
    lang = columns.Text()
    post = columns.Text()
    image = columns.Text()   
    post = columns.Text()
    file_url = columns.Text()
    file_alt = columns.Text()
    #file_width = columns.Integer(default=0)
    #file_height = columns.Integer(default=0)
    url = columns.Text()
    chemin = columns.Text()
    domaine = columns.Text()
    valide = columns.Integer(default=1)
    suprime = columns.Integer(default=0)
    page_url = columns.Text()
    date_timestamp = columns.Integer(default=0)

    #date_creation = columns.DateTime(default=datetime.now)
    date = columns.Text(default=datetime.now().strftime("%d-%m-%Y %H:%M"))
 
    ranking = columns.Integer(default=0)
    ranking_score = columns.Integer(default=0)
    kiffe_nombre = columns.Integer(default=0)
    commentaire_nombre = columns.Integer(default=0)

    def __str__(self):
        return f'{self.utilisateur} {self.post}'
    
    class Meta:
        verbose_name = 'Social'

class KiffeModel(DjangoCassandraModel):
    kiffe_id = columns.Text(primary_key=True)
    social_id = columns.Text(index=True)
    utilisateur_id = columns.Integer()
    utilisateur_url = columns.Text()
    utilisateur = columns.Text()
    fans_id = columns.Integer()
    fans_slug = columns.Text()
    fans = columns.Text()
    suprime = columns.Integer(default=0)
    page_url = columns.Text()
    date = columns.Text(default=datetime.now().strftime("%d-%m-%Y %H:%M"))

    def __str__(self):
        return self.utilisateur_id
    
    class Meta:
        verbose_name = 'kiffe'



class CommentaireModel(DjangoCassandraModel):
    commentaire_id = columns.Text(primary_key=True)
    commenataire = columns.Text()
    social_id = columns.Text(index=True)
    utilisateur_id = columns.Integer()
    utilisateur_url = columns.Text()
    utilisateur = columns.Text()
    fans_id = columns.Integer()
    fans_slug = columns.Text()
    fans = columns.Text()
    suprime = columns.Integer(default=0)
    page_url = columns.Text()
    date = columns.Text(default=datetime.now().strftime("%d-%m-%Y %H:%M"))
    vues = columns.Integer(default=0)

    def __str__(self):
        return self.commentaire
    
    class Meta:
        verbose_name = 'Commentaire'

class FileModel(DjangoCassandraModel):
    file_id = columns.Text(primary_key=True)
    titre = columns.Text()
    file_url = columns.Text()
    file_alt = columns.Text()
    #file_width = columns.Integer(default=0)
    #file_height = columns.Integer(default=0)
    social_id = columns.Text(index=True)
    utilisateur_id = columns.Integer()
    utilisateur_url = columns.Text()
    utilisateur = columns.Text()
    suprime = columns.Integer(default=0)
    page_url = columns.Text()
    date = columns.Text(default=datetime.now().strftime("%d-%m-%Y %H:%M"))
    kiffe_nombre = columns.Integer(default=0)
    vues = columns.Integer(default=0)

    def __str__(self):
        return self.file
    
    class Meta:
        verbose_name = 'File'