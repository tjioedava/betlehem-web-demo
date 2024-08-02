from django.shortcuts import render
from .models import *

def render_home(request):
    context = {'communities': Komunitas.objects.all().values()}

    return render(request, 'home.html', context)

def render_events(request):
    return render(request, 'events.html', dict())

def render_tentang_kami(request):
    return render(request, 'tentang-kami.html', dict())

def render_hubungi_kami(request):
    return render(request, 'hubungi-kami.html', dict())