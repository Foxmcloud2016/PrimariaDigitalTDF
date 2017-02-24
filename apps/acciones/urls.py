from django.conf.urls import url

from .views import AccionCreateView, AccionListView

urlpatterns = [
    url(r'^alta/', AccionCreateView.as_view(), name='alta'),
    url(r'^lista/', AccionListView.as_view(), name='lista'),
]
