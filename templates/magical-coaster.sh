sudo dnf install python3-venv python3-dev redis python3 nginx -y

sudo update-alternatives --config python
mkdir /home/ipn/mvt/
cd /home/ipn/mvt/
python3 -m venv venv
python39 -m venv venv
source venv/bin/activate
chmod 777 -R /home/ipn/mvt
chmod 777 -R /etc/nginx/nginx.conf
chown 777 -R /etc/nginx/nginx.conf
pip install gunicorn gunicorn[gevent] django django-user-agent django-redis django-cassandra-engine psycopg2-binary -y
pip install --upgrade pip

django-admin startproject core .
django-admin startapp utilisateur
django-admin startapp parc
django-admin startapp manege

python manage.py makemigrations
python manage.py migrate 

sudo nano /etc/systemd/system/gunicorn.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target


sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ipn
Group=nginx
WorkingDirectory=/home/ipn/mvt/
ExecStart=/home/ipn/mvt/venv/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock core.wsgi:application

[Install]
WantedBy=multi-user.target

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket

sudo systemctl daemon-reload
sudo systemctl restart gunicorn

sudo firewall-cmd --permanent --add-port=5432/tcp --add-port=9042/tcp --add-port=6379/tcp --add-port=587/tcp 
sudo firewall-cmd --permanent --zone=public --add-service=https --add-service=http

cqlsh -u wivm  51.159.23.160 -p srvo04041987


cql 51.159.23.160


DROP TABLE "Cluster1".utilisateur_model ;
DROP TABLE "Cluster1".transporteur_model ;
DROP TABLE "Cluster1".expediteur_model ;
DROP TABLE "Cluster1".reseau_sociaux_model ;
DROP TABLE "Cluster1".preference_recherche_model ;
DROP TABLE "Cluster1".message_model ;
DROP TABLE "Cluster1".paiement_model ;

DROP TABLE "Cluster1".fret_model ;
DROP TABLE "Cluster1".signalement_model  ;
DROP TABLE "Cluster1".favoris_model ;
DROP TABLE "Cluster1".avis_client_model ;
DROP TABLE "Cluster1".banque_model ;
DROP TABLE "Cluster1".option_fret_model ;
DROP TABLE "Cluster1".mise_relation_model  ;

DROP TABLE "Cluster1".credit_model ;
DROP TABLE "Cluster1".rapport_model ;
DROP TABLE "Cluster1".recherche_fret_model  ;

Keyspace "Cluster1"
-------------------
avis_client_model  fret_model                  rapport_model       
banque_model       message_model               recherche_fret_model
contact_model      mise_relation_model         reseau_sociaux_model
credit_model       option_fret_model           signalement_model   
expediteur_model   paiement_model              transporteur_model  
favoris_model      preference_recherche_model  utilisateur_model