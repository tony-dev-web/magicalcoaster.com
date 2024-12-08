import uuid, os, time
from django.http import HttpResponseRedirect
from utilisateur.models import UtilisateurModel
from urllib.parse import urlparse
from social.models import SocialModel
from PIL import Image, ImageOps
from datetime import datetime



def SocialFormUtils(request, page_url):
    
   if request.method != "POST":
        return HttpResponseRedirect(page_url)
   
   uti = UtilisateurModel.objects.get(utilisateur_id=request.user.id)
   soc1 = SocialModel.objects.create(social_id=uuid.uuid4().hex, utilisateur_id=request.user.id, utilisateur=uti.utilisateur, utilisateur_url=uti.url_frontend, slug=uti.slug, lang=uti.lang)
   soc1.page_url = page_url

   if request.POST['post']:
      soc1.post = request.POST['post']
      
   if request.POST['url']:
      soc1.url = request.POST['url']
      soc1.chemin = urlparse(str(request.POST['url'])).path
      soc1.domaine = urlparse(str(request.POST['url'])).netloc
   
   if request.FILES.get('file', False):
      gg1 = f'img/{ uti.slug }/s-{soc1.social_id}'
      os.makedirs(gg1, exist_ok=True) 
      soc1.file_url = f'/{gg1}/{str(uuid.uuid4().hex)}.jpeg'
      soc1.file_alt = str(soc1.post[:30])
      gg3 = f'.{soc1.file_url}'
      with open(gg3 ,'wb+') as ff:
         ff.write(request.FILES['file'].read())
         ff.close()

      ImageOps.exif_transpose(Image.open(gg3)).rotate(0, fillcolor=(0, 0, 0), expand=True).save(gg3, format="JPEG", optimize=True, quality=85)


   #soc1.date_timestamp = int(time.mktime(datetime.strptime(str(datetime.now()), "%d/%m/%Y").timetuple()))
   soc1.save()

   return HttpResponseRedirect(page_url)

def SocialFormSuprimeUtils(request, social_id):
   soc2 = SocialModel.objects.get(social_id=social_id, suprime=1)
   soc2.save()
   return HttpResponseRedirect(page_url)
