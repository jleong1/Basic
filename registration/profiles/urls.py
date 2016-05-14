from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.profile, name='profile'),
    url(r'^$', views.signup, name='signup'),
    url(r'^$', views.signin, name='signin'),
]
