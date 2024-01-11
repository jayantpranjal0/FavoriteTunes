from django import forms
from .models import Artist,Song  # Import your Artist model from the correct location


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']  # Adjust the fields based on your Artist model

    # You can add custom validation or additional form logic here if needed
    # No two artists have the same Artist
        

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']
