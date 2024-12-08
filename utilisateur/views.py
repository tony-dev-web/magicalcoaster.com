# utilisateur view
from django.shortcuts import get_object_or_404,redirect, render
from django.views import View
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from utilisateur.models import UtilisateurModel
from layout.utils import LayoutUtils 
from social.utils import SocialFormUtils
from social.models import SocialModel
from django.template.defaultfilters import slugify
from utilisateur.utils import Cx2Utils, CompteurUtils

class Cx1View(View):
    url_page = '/cx1/'
    url_page_ok = '/compte/'

    http_method_names = ["get", "post"]
    def get(self,request, lang=None):
        lang = lang or 'fr'
        #ui = get_object_or_404(PageModel, page='connexion')
        
        response = HttpResponse(loader.get_template('a9-cx1.html').render({'layout':LayoutUtils(lang)}, request))
        #response['Link'] = f'<https://wivivi.com{self.url_page}>;rel="canonical", {PreconnectUtils}'
        response['Content-Language'] = lang
        #response.headers['Cache-Control'] = 'public, max-age=10800' 
        return response
    
    def post(self,request, lang=None):
  
        if request.method != "POST":
         #   ErreurUtils('connexion-erreur-post', 0, 0)
            return HttpResponseRedirect(self.url_page)

        email1 = request.POST['email']
        if UtilisateurModel.objects.filter(email=email1).exists():
            redirection_succes = f"/cx2/?email={email1}"
        else :
            redirection_succes = f"/cx3/?email={email1}"

        return HttpResponseRedirect(redirection_succes)

class Cx2View(View):
    url_page = '/cx2/'
    url_page_ok = '/compte/'

    http_method_names = ["get", "post"]
    def get(self,request, lang=None):
        lang = lang or 'fr'
       # ui = get_object_or_404(PageModel, page='connexion-suite')
        
        if not request.GET.get('email', None):
            return redirect(self.url_page_ok)

        response = HttpResponse(loader.get_template('a9-cx2.html').render({'layout':LayoutUtils(lang)}, request))
        response['Content-Language'] = lang
        return response
    
    def post(self,request, lang=None):
        if request.method != "POST":
      #      ErreurUtils('connexion-erreur-post', 0, 0)
            return HttpResponseRedirect(self.url_page)
#
        return Cx2Utils(request, self.url_page)

class Cx3View(View):
    url_page = '/cx3/'
    url_page_ok = '/compte/'

    http_method_names = ["get", "post"]
    def get(self,request, lang=None):
        lang = lang or 'fr'
        #ui = get_object_or_404(PageModel, page='inscription')
        
        if not request.GET.get('email', None):
            return redirect(self.url_page_ok)

        response = HttpResponse(loader.get_template('a9-cx3.html').render({'layout':LayoutUtils(lang)}, request))
        response['Content-Language'] = lang
        return response
    
    def post(self,request, lang=None):
        lang = lang or 'fr'
        if request.method != "POST":
        #    ErreurUtils('erreur-inscription-post',0,0)
            return HttpResponseRedirect(self.url_page)
        
        formulaire_utilisateur = request.POST['utilisateur']
        formulaire_email = request.GET.get('email','')
        formulaire_motpasse1 = request.POST['password']
        formulaire_motpasse2 = request.POST['confirm_password']
        
        if formulaire_motpasse2 != formulaire_motpasse1:
        #    ErreurUtils('erreur-inscription-mot-passe', 0, 0)
        #    messages.info(request, "Email d utilisateur déjà existant ou mot de passe non identique")
            return HttpResponseRedirect(self.url_page)
        
        #elif request.POST['accepte'] == 'false' : 
         #   ErreurUtils('erreur-inscription-accepte', 0, 0)
          #  messages.info(request, 'Vous devez accepter les conditions générales')
          #  return HttpResponseRedirect('/inscription')
        
        elif not UtilisateurModel.objects.filter(email=formulaire_email, utilisateur=formulaire_utilisateur).exists():

            user1 = User.objects.create_user(username=formulaire_email,email=formulaire_email, password=formulaire_utilisateur)
            user1.save()
             
            user_id = int(user1.id)
            uti1 = UtilisateurModel.objects.create(utilisateur_id=user_id, email=formulaire_email, lang=lang, utilisateur=formulaire_utilisateur)
            ut1.slug = slugify(f'{formulaire_utilisateur}-{user_id}')
            uti1.save()

        #    if uti1.utilisateur_id != user1.id :
         #       ErreurUtils('erreur-inscription-id', 0, 0)
         #       messages.info(request, 'erreur id')
        #        return HttpResponseRedirect(self.url_page)


        #    message_email = 'Inscription effectuer avec succès'
        #    EmailUtils(request, emailing=formulaire_email, messaging=message_email, sujeting='Inscription à Wivivi' )
        #    ErreurUtils('inscription-ok', 1, user_id)
        #    messages.info(request, message_email)
        return HttpResponseRedirect('/cx1/')

class MotdepasseView(View):
    http_method_names = ["get", "post"]
    def get(self,request, lang=None):
        lang = lang or 'fr'
       # ui = get_object_or_404(PageModel, page='mot-passe')
        response = HttpResponse(loader.get_template().render({}, request))
        response['Content-Language'] = lang
        #response.headers['Cache-Control'] = 'public, max-age=10800' 
        return response
    
    #def post(self,request, lang=None):
      #  if request.method != "POST":
     #       ErreurUtils('erreur-mot-passe-post', 0, 0)
       #     return HttpResponseRedirect('/connexion/')
#
       # formulaire_email = request.POST['email']
      #  return EmailUtils(request, emailing=formulaire_email, messaging='Mise à jour du mot de passe sur Wivivi', sujeting='Mise à jour du mot de passe sur Wivivi' )


def DeconnexionGet(request, lang=None):
    logout(request)
    request.session.delete()
    return HttpResponseRedirect('/')


#@cache_page(60 * 15)
def UtilisateurGet(request, lang, slug) -> HttpResponse:
    page = get_object_or_404(UtilisateurModel,  slug=slug, valide=1)
    
    up1 = SocialModel.objects.filter(utilisateur_id=page.utilisateur_id)
    
    CompteurUtils(request, ui=page)

    if request.user.is_authenticated :
        SocialFormUtils(request, page_url=page.url_frontend)

    response = render(request, 'a1-utilisateur.html' , context={'page':page,'up1':up1, 'layout':LayoutUtils(lang)}, content_type='text/html')
    response['Link'] = f'<{page.url_frontend}>;rel="canonical"'
    response['Content-Language'] = lang
    #response.headers['Cache-Control'] = 'public, max-age=10800' 
    return response

