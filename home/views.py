from django.shortcuts import render
from .models import Main

def render_home(request):

    main = Main.objects.get(id = 1)
    albums = main.product.albums
    lifes = main.community

    context = {'organization_name': main.name,
               'albums': albums.all().values(),
               'lifes': lifes.all().values()}
    
    return render(request, 'home.html', context)
