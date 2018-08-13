from django.urls import path, re_path
from . import views

urlpatterns = [
    #polls/
    path('', views.index, name='index'),
    #poll/<question_id>
    re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #poll/<question_id>/results
    re_path(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    #poll/<question_id>/vote
    re_path(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
]