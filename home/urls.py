from django.urls import path
from .views import *

urlpatterns = [
    path('home', render_home, name = 'render_home'),
    path('events', render_events, name = 'render_events'),
    path('tentang-kami', render_tentang_kami, name = 'render_tentang_kami'),
    path('hubungi-kami', render_hubungi_kami, name = 'render_hubungi_kami'),
    path('', render_home, name = 'render_home'),
]