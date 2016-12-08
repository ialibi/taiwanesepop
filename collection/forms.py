from django.forms import ModelForm
from collection.models import Song

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('name', 'description',)
