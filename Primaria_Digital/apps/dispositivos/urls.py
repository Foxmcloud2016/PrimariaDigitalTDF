from django.conf.urls import url
from .views import DispositivosView, EscuelaDispositivosView, CreateAdm


urlpatterns = [
    url(r'^alta/adm',CreateAdm.as_view(),name='alta_adm'),
    url(r'^lista/',DispositivosView.as_view(),name='lista'),
    url(r'^dispo_list/',EscuelaDispositivosView.as_view(),name='listado_disp')
]
