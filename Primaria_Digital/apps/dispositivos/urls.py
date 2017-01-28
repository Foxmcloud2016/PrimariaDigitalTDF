from django.conf.urls import url
from .views import DispositivosView, EscuelaDispositivosView


urlpatterns = [
    url(r'^lista/',DispositivosView.as_view(),name='lista'),
    url(r'^dispo_list/',EscuelaDispositivosView.as_view(),name='listado_disp')
]
