from django.core.mail import EmailMessage, get_connection
from django.shortcuts import redirect
from django.contrib.auth import authenticate , login
from utilisateur.models import UtilisateurModel
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.sessions.exceptions import SessionInterrupted

def Cx2Utils(request, self):
    formulaire_email = request.GET.get('email','')
    formulaire_motpasse = request.POST['password']
    user = authenticate(username=formulaire_email,password=formulaire_motpasse)
    if user is None:
        #ErreurUtils('connexion-erreur-authentification', 0, 0)
        #messages.info(request, 'Erreur de connexion')
        return redirect(self.url_page)
    else:
        login(request, user)

        try:
            request.session.save()
        except:
            raise SessionInterrupted("erreur cookie") from e
        
        #sujet_email= 'Connexion à Wivivi'
        #message_email = 'Connexion effectuer avec succès'
        #EmailUtils(request, emailing=formulaire_email, messaging=message_email, sujeting=sujet_email )  
        #ErreurUtils( 'connexion-ok', 1, request.user.id )
        #response.set_cookie('sessionid', request.session.session_key,max_age=1209600, domain='wivivi.com',path='/',secure=True, httponly=True,samesite=None,)
        return HttpResponseRedirect(self.url_page)

def CompteurUtils(request, ui) -> None:
    if not request.user_agent.is_bot:
        ui.vues += 1
        return ui.save()