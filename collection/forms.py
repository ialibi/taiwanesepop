from django import forms
from collection.models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('name', 'description',)

