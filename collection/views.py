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
        'song': song
    })	

def edit_song(request, slug):
    song = Song.objects.get(slug=slug)

    # set the form we're using...
    form_class = SongForm

    # if we're coming to this view from a submitted form,  
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=song)

        if form.is_valid():
            # save the new data
            form.save()
            return redirect('song_detail', slug=song.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=song)

    # and render the template
    return render(request, 'songs/edit_song.html', {
        'song': song,
        'form': form,
    #form=SongForm()
    #return render(request, 'songs/edit_song.html', {
    #	'form': form
    })	    

