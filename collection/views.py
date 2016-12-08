from django.shortcuts import render, redirect
from collection.forms import SongForm
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

def edit_song(request, slug):
    song = Song.objects.get(slug=slug)
    form_class = SongForm
    #add the following line from checking stack overflow, not from the tutorial
    form = form_class(request.POST or None)
    if request.method == 'POST':
      form = form_class(data=request.POST, instance=song)
      if form.is_valid():
         form.save()
         return redirect('song_detail', slug=song.slug)
      else:
        form = form_class(instance=song)
    return render(request, 'songs/edit_song.html', {
      	'song': song,
      	'form': form,
      }) 	        	  	
	
def browse_by_name(request, initial=None):
    if initial:
       songs = Song.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        songs = Song.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'songs': songs,
        'initial': initial,
    })   
