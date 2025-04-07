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
        'signup/',
        views.signup,
        name='signup',
        ),
    path(
        'synths/',
        views.SynthListView.as_view(),
        name='synth_list',
        ),
    path(
        'synths/new/',
        views.SynthCreateView.as_view(),
        name='synth_create',
        ),
    path(
        'synths/<int:pk>/',
        views.synth_detail,
        name='synth_detail',
        ),
    path(
        'synths/<int:pk>/edit/',
        views.SynthUpdateView.as_view(),
        name='synth_update',
        ),
    path(
        'synths/<int:pk>/delete/',
        views.SynthDeleteView.as_view(),
        name='synth_delete'
        ),
    path(
        'logs/<int:pk>/edit/', views.SynthLogUpdateView.as_view(),
        name='log_edit',
    ),
    path(
        'logs/<int:pk>/delete/', views.SynthLogDeleteView.as_view(),
        name='log_delete',
    ),
]