from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name='home',
        ),
    path('about/',
        views.about,
        name='about',
        ),
    path(
        'synths/',
        views.synth_index,
        name='synth_index',
        ),
    path(
        'synths/create/',
        views.synth_create,
        name='synth_create',
        ),
    path(
        'synths/<int:synth_id>/',
        views.synth_detail,
        name='synth_detail',
        ),
    path(
        'synths/<int:synth_id>/update/',
        views.synth_update,
        name='synth_update',
        ),
    path(
        'synths/<int:synth_id>/',
        views.synth_delete,
        name='synth_delete'
        ),
]