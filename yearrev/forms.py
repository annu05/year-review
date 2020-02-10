from django import forms

from .models import Anime
from .models import Manga
from .models import Movie

from .models import Drawing
from .models import Book


class Animeform(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ('title', 'image', 'rating', 'startdate', 'startmonth', 'startyear', 'enddate', 'endmonth', 'endyear')

class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'image', 'rating', 'date', 'month', 'year')

