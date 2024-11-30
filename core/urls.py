from django.contrib import admin
from django.urls import path
from layout.views import IndexGet

urlpatterns = [
    path('adadad/', admin.site.urls),
    path('', IndexGet),
]
