from django.urls import path
from . import views
from . import views as core_views

urlpatterns =[
    path('',views.base,name='base'),
    path('anime',views.anime,name='anime'),
    path('anime/add',views.animeadd,name='animeadd'),
    path('movie',views.movie,name='movie'),
    path('movie/add',views.movieadd,name='movieadd'),
    path('game', views.game, name='game'),
    path('manga', views.manga, name='manga'),
    path('book', views.book, name='book'),
]