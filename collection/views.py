from django.shortcuts import render
from collection.models import Song

def index(request):
	songs=Song.objects.all()
	return render(request, 'index.html', {
		'songs': songs,
	})

def song_detail(request, slug):
    # grab the object...
    song = Song.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'songs/song_detail.html', {
        'song': song,
    })	
