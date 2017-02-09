from django.conf.urls import url
from .views import DispositivosView, EscuelaDispositivosView, CreateAdm, DispositivoCreateView,NetbookFormMassiveView


urlpatterns = [
    url(r'^alta/dispositivo/netbooks/(?P<id_adm>[0-9]+)/',NetbookFormMassiveView.as_view(),name='alta_netbook'),
    url(r'^alta/dispositivo/(?P<id_adm>[0-9]+)-(?P<n_tipo>[0-9]+)/',DispositivoCreateView.as_view(),name='alta_dispositivo'),
    url(r'^alta/adm',CreateAdm.as_view(),name='alta_adm'),
    url(r'^lista/',DispositivosView.as_view(),name='lista'),
    url(r'^dispo_list/',EscuelaDispositivosView.as_view(),name='listado_disp')
]
