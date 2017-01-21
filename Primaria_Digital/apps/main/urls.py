from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import HomeView

urlpatterns = [
    url(r'^home/$', login_required(HomeView.as_view()), name='home'),
]
