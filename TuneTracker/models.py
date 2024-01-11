from django.db import models

# Create your models here.


class Artist(models.Model):
    
        name = models.CharField(max_length=200)
    
        def __str__(self):
            return self.name
        
        def get_songs(self):
            return Song.objects.filter(artist=self)
        
        def get_song_count(self):
            return Song.objects.filter(artist=self).count()
        
        def get_all_artists_with_song_count():
            return Artist.objects.annotate(song_count=models.Count('song'))
        

class Song(models.Model):

    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
         return self.title+" - "+self.artist.name
    