from django.forms import ModelForm
from .models import Main

class AlbumForm(ModelForm):
    class Meta:
        model = Main
        fields = '__all__'