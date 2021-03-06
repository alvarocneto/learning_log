"""Define padrões de url para learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Pagina Inicial
    url(r'^$', views.index, name='index'),

    # Mostra todos os assuntos
    url(r'^topics/$', views.topics, name='topics'),

    # Mostra de detalhes do tópico
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Cadastro de um novo tópico
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Cadastro de uma nova entrada
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Editando uma entrada
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
]
