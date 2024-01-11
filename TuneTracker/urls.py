from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.artists, name='artists'),
    path('songs/', views.songs, name='songs'),
    path('artist/<int:artist_id>/', views.artist, name='artist'),
    path('song/<int:song_id>/', views.song, name='song'),
    path("add_artist/",views.add_artist,name='add_artist'),
    path("add_song/",views.add_song,name='artist_song')
]