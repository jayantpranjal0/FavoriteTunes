from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect

# Create your views here.


def index(request):
    return render(request, 'TuneTracker/index.html')

def artists(request):
    # artists=Artist.objects.all()
    # context = {'artists': artists}

    artists=Artist.get_all_artists_with_song_count()
    context = {'artists': artists}


    return render(request, 'TuneTracker/artists.html', context)

def songs(request):
    songs=Song.objects.all()
    context = {'songs': songs}
    return render(request, 'TuneTracker/songs.html', context)

def artist(request, artist_id):
    artist=Artist.objects.get(id=artist_id)
    context = {'artist': artist, 'songs': artist.get_songs()}
    print(context)
    return render(request, 'TuneTracker/artist.html', context)

def song(request, song_id):
    print("Reached here")
    song=Song.objects.get(id=song_id)
    context = {'song': song}
    return render(request, 'TuneTracker/song.html', context)

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artists')
    else:
        form = ArtistForm()
    return render(request, 'TuneTracker/add_artist.html', {'form': form})


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('songs')
    else:
        form = SongForm()
    return render(request, 'TuneTracker/add_song.html', {'form': form})

