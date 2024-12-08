# utilisateur view
import uuid, os
from django.shortcuts import get_object_or_404
from django.views import View
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.template.defaultfilters import slugify
from django import forms
from utilisateur.models import UtilisateurModel
from layout.utils import LayoutUtils
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

#Parc
class Fut1View(View):
    url_page = '/fut1/'
    url_page_ok = '/compte/'
    http_method_names = ["get", "post"]
    def get(self,request,parc_id=None, lang=None):
        lang = lang or 'fr'
        uti = get_object_or_404(UtilisateurModel, utilisateur_id=request.user.id )

        response = HttpResponse(loader.get_template('a8-fut1.html').render({'uti':uti,'layout':LayoutUtils(lang)}, request))
        #response['Link'] = PreconnectUtils
        response['Content-Language'] = lang
        #response.headers['Cache-Control'] = 'public, max-age=10800' 
        return response
    
    def post(self,request, lang=None):
        form = UploadFileForm(request.POST, request.FILES)
        if request.method != "POST":
            #ErreurUtils('connexion-erreur-post', 0, 0)
            return HttpResponseRedirect(f'/fr{self.url_page}')

   
        fut1 = UtilisateurModel.objects.get(utilisateur_id=request.user.id)
        fut1.titre = fut1.utilisateur
        fut1.description = request.POST['description']

        fut1.adresse = request.POST['adresse']
        #fut1.code_postale = request.POST['code_postale']
        fut1.ville = request.POST['ville']
        fut1.pays = request.POST['pays']
        fut1.site_web = request.POST['site_web']

        fut1.parc_prefere = request.POST['parc_prefere']
        fut1.manege_prefere = request.POST['manege_prefere']
        fut1.coaster_prefere = request.POST['coaster_prefere']
        fut1.hotel_prefere = request.POST['hotel_prefere']
        fut1.land_prefere = request.POST['land_prefere']
        fut1.spectacle_prefere = request.POST['spectacle_prefere']
        fut1.boutique_prefere = request.POST['boutique_prefere']
        fut1.restaurant_prefere = request.POST['restaurant_prefere']
        
        if form.is_valid():
            if request.FILES['img1']:
                gg1 = f'img/{ fut1.slug }/u-{fut1.utilisateur_id}'
                os.makedirs(gg1, exist_ok=True) 
                #tra1.profil_image  = f'/{gg1}/{tra1.profil_slug}.avif'
                fut1.photo  = f'/{gg1}/{str(uuid.uuid4().hex)}.avif'
                fut1.photo_alt  = fut1.utilisateur
                gg3 = f'.{fut1.photo}'
                with open(gg3 ,'wb+') as ff:
                    ff.write(request.FILES['img1'].read())
                    ff.close()

        fut1.save()
        return HttpResponseRedirect(f'/{fut1.lang}{self.url_page}')