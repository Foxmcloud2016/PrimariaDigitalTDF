from django.conf.urls import url
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    url(r'^registrar/$',RegisterView.as_view() , name='register'),
    url(r'^login/',LoginView.as_view() , name='login'),
    url(r'^salir/$',LogoutView.as_view() , name='logout'),
]
