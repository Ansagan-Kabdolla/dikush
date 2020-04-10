from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('contacts', contacts, name='contacts'),
    path('ethicks', ethicks, name='ethicks'),
    path('gid', gid, name='gid'),
    path('predmeti/<name>', seria, name='predmet'),
    path('add/', PdfCreateView.as_view(), name='add'),
    path('articles/', articles, name='articles'),
    path('all_files/', all_files, name='all_files'),
]