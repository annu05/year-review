from django.contrib import admin

from .models import *

admin.site.register(Anime)
admin.site.register(Movie)

admin.site.register(Manga)
admin.site.register(Book)
admin.site.register(Drawing)