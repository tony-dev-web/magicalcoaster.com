from django.contrib import admin
from django.urls import path
from utilisateur.views import Cx1View, Cx2View, Cx3View, DeconnexionGet, UtilisateurGet
from utilisateur.viewsform import Fut1View
from layout.views import IndexGet, CompteGet, MentionsGet
from parc.views import ParcGet, LandGet, HotelGet,BoutiqueGet,SpectacleGet,RestaurantGet,CoasterGet,ManegeGet
from parc.viewsform import Fpa1View, Fla2View, Fho6View, Fsp7View, Fma3View, Fco8View, Fre4View, Fbo5View
from parc.views import ListeParcView, ListeLandView, ListeHotelView, ListeBoutiqueView, ListeSpectacleView, ListeUtilisateurView, ListeRestaurantView, ListeCoasterView, ListeManegeView
from core.decorators import login_connect, login_non_connect

urlpatterns = [
    path('', IndexGet),
    path('cx1/', Cx1View.as_view()),
    path('cx2/', Cx2View.as_view()),
    path('cx3/', Cx3View.as_view()),
    path('cx9/', DeconnexionGet),
    path('compte/', login_connect(CompteGet)),
    path('<str:lang>/parcs/', ListeParcView.as_view(), name="parc_url_liste"),
    path('<str:lang>/parcs/', ParcGet, name="parc_url"),
    path('<str:lang>/lands/', ListeLandView.as_view(), name="land_url_liste"),
    path('<str:lang>/lands/<str:slug>', LandGet, name="land_url"),
    path('<str:lang>/hotels/', ListeHotelView.as_view(), name="hotel_url_liste"),
    path('<str:lang>/hotels/<str:slug>', HotelGet, name="hotel_url"),
    path('<str:lang>/boutiques/', ListeBoutiqueView.as_view(), name="boutique_url_liste"),
    path('<str:lang>/boutiques/<str:slug>', BoutiqueGet, name="boutique_url"),
    path('<str:lang>/spectacles/', ListeSpectacleView.as_view(), name="spectacle_url_liste"),
    path('<str:lang>/spectacles/<str:slug>', SpectacleGet, name="spectacle_url"),
    path('<str:lang>/fans/', ListeUtilisateurView.as_view()),
    path('<str:lang>/fans/<str:slug>', UtilisateurGet, name="utilisateur_url"),
    path('<str:lang>/restaurants/', ListeRestaurantView.as_view(), name="restaurant_url_liste"),
    path('<str:lang>/restaurants/<str:slug>', RestaurantGet, name="restaurant_url"),
    path('<str:lang>/coasters/', ListeCoasterView.as_view(), name="coaster_url_liste"),
    path('<str:lang>/coasters/<str:slug>', CoasterGet, name="coaster_url"),
    path('<str:lang>/maneges/', ListeManegeView.as_view(), name="manege_url_liste"),
    path('<str:lang>/maneges/<str:slug>', ManegeGet, name="manege_url"),
    path('<str:lang>/fpa1/', Fpa1View.as_view()),
    path('<str:lang>/fla2/', Fla2View.as_view()),
    path('<str:lang>/fho6/', Fho6View.as_view()),
    path('<str:lang>/fbo5/', Fbo5View.as_view()),
    path('<str:lang>/fsp7/', Fsp7View.as_view()),
    path('<str:lang>/fut1/', Fut1View.as_view()),
    path('<str:lang>/fre4/', Fre4View.as_view()),
    path('<str:lang>/fco8/', Fco8View.as_view()),
    path('<str:lang>/fma3/', Fma3View.as_view()),
    path('<str:lang>/mentions-legales/', MentionsGet, name="mentions_url")]
