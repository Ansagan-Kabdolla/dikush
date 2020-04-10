from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView
from .forms import PdfForm

class PdfCreateView(CreateView):
    model=Filepdf
    template_name = 'publication/add.html'
    form_class = PdfForm
    success_url = '/articles'


def index(request):
    return render(request,'publication/index.html')


def contacts(request):
    return render(request,'publication/contacts.html')


def ethicks(request):
    return render(request,'publication/ethicks.html')


def gid(request):
    return render(request,'publication/gid.html')


def seria(request,name):
    preds = Predmeti.objects.get(name=name)
    return render(request,'publication/seria.html',{'preds':preds})

def articles(request):
    publs = Filepdf.objects.all()[:6]
    return render(request,'publication/article.html',{'publs':publs})

def all_files(request):
    publs = Filepdf.objects.all()
    return render(request,'publication/all_files.html',{'publs':publs})