from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Main
from .forms import AlbumForm

def render_home(request):

    main = Main.objects.get(id = 1)
    albums = main.product.albums
    lifes = main.community

    context = {'organization_name': main.name,
               'albums': albums.all().values(),
               'lifes': lifes.all().values()}
    
    return render(request, 'home.html', context)

def render_form(request):
    
    form = AlbumForm()

    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if(form.is_valid()):
            form.save()
            form = AlbumForm()

    context = {'form': form}

    return render(request, 'form.html', context)