from django.conf.urls import url

from .views import AccionCreateView

urlpatterns = [
    url(r'^alta/', AccionCreateView.as_view(), name='alta'),
]
