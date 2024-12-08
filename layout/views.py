from django.shortcuts import get_object_or_404,redirect, render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from layout.models import PageModel
from layout.utils import LayoutUtils
from social.utils import SocialFormUtils
from social.models import SocialModel
from utilisateur.models import UtilisateurModel
PreconnectUtils = ''


#@cache_page(60 * 15)
def IndexGet(request,lang=None) -> HttpResponse:
    lang = lang or 'fr'
    url_page = 'https://magicalcoaster.com/'
    #RechercheUtils(request)
    
    #cache_key = f'index_get_{request.user.is_authenticated}'
    #page = cache.get(cache_key)
    #if ui is None:
    page = get_object_or_404(PageModel, page='index')
        #cache.set(cache_key, ui, 60 * 15) # Cache l'objet pendant 15 minutes
    
    if request.user.is_authenticated :
        SocialFormUtils(request, page_url='/')

    up1 = SocialModel.objects.filter(valide=1)

    response = render(request, 'a1-index.html' , context={'page':page, 'layout':LayoutUtils(lang), 'up1':up1}, content_type='text/html')
    response['Link'] = f'<{url_page}>;rel="canonical", {PreconnectUtils}'
    response['Content-Language'] = lang
    #response.headers['Cache-Control'] = 'public, max-age=10800' 
    return response


#@cache_page(60 * 15)
def CompteGet(request,lang=None) -> HttpResponse:
    lang = lang or 'fr'
    page = get_object_or_404(PageModel, page='compte')
    uti = UtilisateurModel.objects.get(utilisateur_id=request.user.id)
    response = render(request, 'a8-compte.html' , context={'page':page,'uti':uti,  'layout':LayoutUtils(lang)}, content_type='text/html')
    response['Content-Language'] = lang
    #response.headers['Cache-Control'] = 'public, max-age=10800' 
    return response

#@cache_page(60 * 15)
def MentionsGet(request,lang=None) -> HttpResponse:
    lang = lang or 'fr'
    page = get_object_or_404(PageModel, page='mentions')
    
    response = render(request, 'a1-mentions.html' , context={'page':page, 'layout':LayoutUtils(lang)}, content_type='text/html')
    response['Link'] = f'<{ page.url }>;rel="canonical", {PreconnectUtils}'
    response['Content-Language'] = lang
    #response.headers['Cache-Control'] = 'public, max-age=10800' 
    return response