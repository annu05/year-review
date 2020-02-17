from django.urls import path
from . import views
from . import views as core_views

urlpatterns =[
    path('',views.base,name='base'),
    path('anime/year/<int:pk>',views.anime,name='anime'),
    path('anime/year/',views.animeyear,name='animeyear'),
    path('anime/add',views.animeadd,name='animeadd'),
    path('anime/edit/<int:pk>/',views.editanime,name='editanime'),
    path('movie/year/<int:pk>',views.movie,name='movie'),
    path('movie/year/',views.moviesyear,name='movieyear'),
    path('movie/add',views.movieadd,name='movieadd'),
    path('game/year/2020', views.game, name='game2020'),
    path('game/year/2019', views.game2019, name='game2019'),
    path('game/year/2018', views.game2018, name='game2018'),
    path('game/year', views.gameyear, name='gameyear'),
    path('manga', views.manga, name='manga'),
    path('book', views.book, name='book'),
    path('drawing/year/',views.drawingyear,name='drawingyear'),
    path('drawing/year/<int:pk>',views.drawing,name='drawing'),

]