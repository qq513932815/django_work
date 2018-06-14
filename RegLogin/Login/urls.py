from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/action', views.login_action, name='login_action'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/action', views.reg_action, name='reg_action'),


]