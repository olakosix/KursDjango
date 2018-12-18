from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import Template, Context, loader, context

from .models import Wpis

def index (request):
    wpisy = Wpis.objects.all()
    wynik =""
    for w in wpisy:
        wynik += f"{w.tytul}<br>"

    return HttpResponse (wynik)

def index_temp(request):
    t= loader.get_template('blog/index.html')
    Context = {'chleb':'1,90',
               'woda': 1.80}
    wynik = t.render(context)

    return render(request=request, template_name='blog/index.html', context=context)


