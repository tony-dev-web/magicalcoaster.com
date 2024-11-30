
from django.shortcuts import get_object_or_404,redirect, render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect




#@cache_page(60 * 15)
def IndexGet(request,lang=None) -> HttpResponse:
    lang = lang or 'fr'
    url_page = 'https://magicalcoaster.com/'
    #RechercheUtils(request)
    
    #cache_key = f'index_get_{request.user.is_authenticated}'
    #ui = cache.get(cache_key)
    #if ui is None:
    #ui = get_object_or_404(PageModel, page='europe')
        #cache.set(cache_key, ui, 60 * 15) # Cache l'objet pendant 15 minutes
    #if request.GET.get('ref'):
       # return HttpResponseRedirect(url_page)
    
    response = render(request, 'a1-index.html' , context={}, content_type='text/html')
    #response['Link'] = f'<{url_page}>;rel="canonical", {PreconnectUtils}'
    response['Content-Language'] = lang
    #response.headers['Cache-Control'] = 'public, max-age=10800' 
    return response
