from django.shortcuts import render

def render_home(request):
    context = {}
    return render(request, 'home.html', context)
