from django.contrib import admin
from social.models import SocialModel, KiffeModel, CommentaireModel, FileModel

admin.site.register([SocialModel, KiffeModel, CommentaireModel, FileModel])