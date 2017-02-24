from django.conf.urls import url
from .views import EscuelaCreateView,EscuelaUpdateView,ListaEscuelasView


urlpatterns = [
    url(r'^alta/$', EscuelaCreateView.as_view(), name='alta'),
    url(r'^modificar/(?P<pk>[0-9]+)/$', EscuelaUpdateView.as_view(), name='modificar'),
    url(r'^lista/$', ListaEscuelasView.as_view(), name='lista'),
]
